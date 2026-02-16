# ---- Base Image ----
FROM python:3.12-slim

# ---- Set environment variables ----
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=kamate_group_main.settings
ENV SECRET_KEY="temporary_secret_key_for_docker_build"

# ---- Install system dependencies ----
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    git \
    nodejs \
    npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ---- Set workdir ----
WORKDIR /app

# ---- Copy requirements and install Python deps ----
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ---- Copy project files ----
COPY . .

# ---- Install Node/Tailwind dependencies ----
# Adjust 'theme' folder to your Tailwind app folder
WORKDIR /app/theme
RUN npm install

# ---- Switch back to project root ----
WORKDIR /app

# ---- Build Tailwind CSS & collect static files ----
RUN python manage.py tailwind build
RUN python manage.py collectstatic --noinput

# ---- Expose port ----
EXPOSE 10000

# ---- Start Gunicorn ----
CMD ["gunicorn", "kamate_group_main.wsgi:application", "--bind", "0.0.0.0:10000"]
