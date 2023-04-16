FROM python:3.9-alpine AS base

FROM base AS build

# We need to build cffi, so we will use multi-stage build
RUN apk add --no-cache build-base libffi-dev openssl-dev \
    && pip install --no-cache-dir -U pip

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

#################################
FROM base AS prod

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# RUN apk add libjpeg libstdc++ --no-cache
# COPY --from=build /usr/lib/ /usr/lib/
COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/
COPY scripts/docker-entrypoint.sh scripts/docker-healthcheck.sh ./
RUN chmod +x ./docker-entrypoint.sh ./docker-healthcheck.sh

# COPY alembic.ini ./alembic.ini
# COPY migrations ./migrations
COPY static ./static
COPY templates ./templates
COPY app ./app

EXPOSE 8000
# HEALTHCHECK --interval=30s --timeout=5s --retries=5 \
#     CMD ["/app/docker-healthcheck.sh"]

ENTRYPOINT ["/app/docker-entrypoint.sh"]