#!/bin/bash

echo ">>>>>>Starting deploy<<<<<<"

echo ">>>>>>Stopping port running server before..."
kill -9 `sudo lsof -t -i:8000`
echo ">>>>>>Create virtual env..."
python3 -m venv env

# source python env
echo ">>>>>>Sourcing python env..."
. env/bin/activate

# install requirements
pip install -r requirements.txt

# migrate model
echo "Migrate model..."
python manage.py migrate

# run server
echo "Run server..."
JENKINS_NODE_COOKIE=dontKillMe nohup python manage.py runserver 0:8000 > my.log 2>&1 &