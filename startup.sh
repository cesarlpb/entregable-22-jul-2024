  #!/bin/bash

  # Cambiar solo carpeta proyecto
  cd <carpeta_de_proyecto>

  # NO CAMBIAR:
  # Creamos .venv:
  python -m venv .venv
  # Activamos .venv:
  source .venv/bin/activate
  # Instalo pips:
  pip install -r requirements.txt
  # Comandos de Django:
  python manage.py collectstatic --noinput # si arroja error, revisar STATIC_ROOT
  python manage.py makemigrations && python manage migrate
  python manage.py runserver
  # NO CAMBIAR ^^^