  #!/bin/bash

  # Cambiar solo carpeta proyecto
  cd <carpeta_de_proyecto>

  # NO CAMBIAR:
  python -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  python manage.py collectstatic --noinput # si arroja error, revisar STATIC_ROOT
  python manage.py makemigrations && python manage migrate
  python manage.py runserver
  # NO CAMBIAR ^^^