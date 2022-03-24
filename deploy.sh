#!/bin/bash

echo ">>>>>>Starting deploy<<<<<<"
echo ">>>>>>Create virtual env..."
python3 -m venv env

# source python env
echo ">>>>>>Sourcing python env..."
source env/bin/activate

# install requirements
pip install -r requirements.txt

# migrate model
echo "Migrate model..."
python manage.py migrate

# run tests
echo "Run server..."
sudo gunicorn core.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --daemon