#!/usr/bin/env bash

pip install -r requirements.txt

echo "========== MEDIA =========="
find media -type f

python manage.py collectstatic --noinput

python manage.py migrate