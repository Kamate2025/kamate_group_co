# ---- Base Image ----
FROM python:3.12-slim

# ---- Set work directory ----
WORKDIR /app

# ---- Install system dependencies ----
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy Python dependencies ----
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ---- Copy project files ----
COPY . .

# ---- Set environment variables ----
# SECRET_KEY fallback for build-time (can be overridden in Render settings)
ENV SECRET_KEY="temporarysecretkey123"
ENV DEBUG=True
ENV ALLOWED_HOSTS="*"

# ---- Build Tailwind CSS & collect static files ----
RUN python manage.py tailwind build
RUN python manage.py collectstatic --noinput

# ---- Expose port ----
EXPOSE 8000

# ---- Start server ----
# Migrate DB, then run Gunicorn
CMD python manage.py migrate --noinput && \
    gunicorn kamate_group_main.wsgi:application --bind 0.0.0.0:8000
