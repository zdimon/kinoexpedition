# Одностраничный сайт на Django

## Деплой
    git clone git@github.com:zdimon/kinoexpedition.git
    cd kinoexpedition
    virtualenv -p python3 venv
    . ./venv/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py load_data
    ./manage.py runserver
