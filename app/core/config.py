import datetime
import os
import typing

import dotenv
import pydantic
import yaml
from pydantic.env_settings import SettingsSourceCallable

dotenv.load_dotenv()


def yaml_config_settings_source(
    settings: pydantic.BaseSettings,
) -> typing.Dict[str, typing.Any]:
    encoding = settings.__config__.env_file_encoding
    filename = os.environ.get("CONFIG_FILE", "config.yml")
    if not os.path.exists(filename):
        return {}

    with open(filename, encoding=encoding) as f:
        return yaml.safe_load(f)


class Settings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"
        extra = "ignore"

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> typing.Tuple[SettingsSourceCallable, ...]:
            return (
                init_settings,
                file_secret_settings,
                env_settings,
                yaml_config_settings_source,
            )


settings = Settings()  # type: ignore

print(settings)
