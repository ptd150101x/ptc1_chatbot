#!/bin/sh

# exit on error
set -e

echo "Waiting for Postgres..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Postgres started"

echo "Running migrations..."
if alembic upgrade head; then
  echo "Migrations completed successfully"
else
  echo "Migration failed"
  exit 1
fi

echo "Starting application..."
if [ "$ENVIRONMENT" = "development" ]; then
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else
  uvicorn app.main:app --host 0.0.0.0 --port 8000
fi
