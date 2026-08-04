#!/usr/bin/env bash

pip install -r requirements.txt

echo "========== PROJECT FILES =========="
pwd
ls -la

echo "========== MEDIA =========="
ls -R media || echo "MEDIA DIRECTORY NOT FOUND"

python manage.py collectstatic --noinput

python manage.py migrate