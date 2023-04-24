# Habit Tracker

## Local setup

```bash
cp .env.example .env
python -m venv venv

# in activated virtual environment
pip install -r requirements.txt

# apply migrations to database
python manage.py migrate

# Optional: create superuser
python manage.py createsuperuser

# run development server
python manage.py runserver
```
