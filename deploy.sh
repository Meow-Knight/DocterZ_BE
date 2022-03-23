# source python env
echo ">>>>>>Sourcing python env..."
source "env/bin/activate"

# install requirements
pip install -r requirements.txt

# migrate model
echo "Migrate model..."
python manage.py migrate

# run tests
echo "Run server..."
python manage.py runserver 0:8000