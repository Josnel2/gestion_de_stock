#!/script/bash

set -e
source /opt/env/scripts/activate

if [ "$1" = "gunicorn" ]; then

exec gunicorn gest_stock.wsgi:application --bind 0.0.0.0:8000 --workers 3
else

python manage.py runserver 0.0.0.0:8000

fi

