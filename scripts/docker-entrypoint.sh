#!/bin/sh

set -e

# Apply database migrations
if command -v alembic &> /dev/null
then
    alembic upgrade head
fi

# Start Gunicorn
exec gunicorn \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers ${GUNICORN_WORKERS:-$(nproc)} \
    --worker-class ${GUNICORN_WORKER_CLASS:-uvicorn.workers.UvicornWorker} \
    --access-logfile - \
    --error-logfile - \
    --proxy-allow-from='*' \
    app.api:server \
    $@
