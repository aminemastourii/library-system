#!/bin/bash

# Exit on any error
set -e

echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Populating the database..."
python populate_books.py

echo "Starting the Django server..."
exec "$@"
