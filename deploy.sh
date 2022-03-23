echo ">>>>>>Starting deploy<<<<<<"
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

# run tests
echo "Run server..."
python manage.py runserver 0:8000