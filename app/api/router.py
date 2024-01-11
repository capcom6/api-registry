import glob
import itertools
import os
import shutil
import tempfile
import zipfile

import fastapi
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = fastapi.APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    path_static = "./static"
    path_apis = os.path.join(path_static, "apis")
    apis = [
        {
            "path": p.replace(path_static, "", 1),
            "name": os.path.splitext(os.path.basename(p))[0],
            "group": os.path.split(os.path.dirname(p))[1],
        }
        for p in glob.glob(os.path.join(path_apis, "**/*.yaml"), recursive=True)
    ]
    apis = sorted(apis, key=lambda item: item["group"])
    grouped_apis = {}
    for key, values in itertools.groupby(apis, lambda item: item["group"]):
        grouped_apis[key] = sorted(values, key=lambda item: item["path"])

    return templates.TemplateResponse(
        "index.html", {"request": request, "api_groups": grouped_apis}
    )


@router.put("/api/v1/apis", status_code=204)
async def put_apis(file: fastapi.UploadFile):
    folder_path = "./static/apis"
    # Check if folder exists
    if not os.path.isdir(folder_path):
        raise fastapi.HTTPException(500, f"{folder_path} is not a valid directory")

    with tempfile.TemporaryDirectory() as tmpdir:
        with tempfile.TemporaryFile() as tmpfile:
            # Copy the contents of the upload file to the temporary file
            shutil.copyfileobj(file.file, tmpfile)
            tmpfile.seek(0)
            try:
                with zipfile.ZipFile(tmpfile, "r") as zip_ref:
                    zip_ref.extractall(tmpdir)
            except zipfile.BadZipFile:
                raise fastapi.HTTPException(
                    400, "Uploaded file is not a valid zip file"
                )

        # Replace the contents of the folder with the contents of the zip file
        shutil.rmtree(folder_path, ignore_errors=True)
        shutil.copytree(tmpdir, folder_path, dirs_exist_ok=True)
