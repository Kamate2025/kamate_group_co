# ---- Base image ----
FROM python:3.12-slim

# ---- Environment variables ----
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=kamate_group_main.settings
ENV SECRET_KEY="temporary_secret_key_for_docker_build"

# ---- Install system dependencies ----
RUN apt-get update && apt-get install -y \
    curl build-essential git nodejs npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ---- Set working directory ----
WORKDIR /app

# ---- Install Python dependencies ----
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ---- Copy project files ----
COPY . .

# ---- Tailwind build ----
WORKDIR /app/theme/static_src
RUN npm install
WORKDIR /app
RUN python manage.py tailwind build

# ---- Collect static files ----
RUN python manage.py collectstatic --noinput

# ---- Expose port & run ----
EXPOSE 10000
CMD python manage.py migrate --noinput && \
    python manage.py shell -c "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
username='Kamate20252026'; \
password='Kamate@215'; \
email='admin@example.com'; \
if not User.objects.filter(username=username).exists(): \
    User.objects.create_superuser(username, email, password)" && \
    gunicorn kamate_group_main.wsgi:application --bind 0.0.0.0:10000
