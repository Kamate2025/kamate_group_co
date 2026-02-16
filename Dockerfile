# 1. Use official Python image
FROM python:3.12-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Copy project code
COPY . .

# 6. Set temporary environment variables for Django
ENV SECRET_KEY='temporarysecretkey123'
ENV DEBUG=True
ENV ALLOWED_HOSTS='*'

# 7. Build Tailwind CSS
RUN python manage.py tailwind build

# 8. Collect static files
RUN python manage.py collectstatic --noinput

# 9. Expose port 8000
EXPOSE 8000

# 10. Run migrations & start gunicorn
CMD python manage.py migrate --noinput && \
    gunicorn kamate_group_main.wsgi:application --bind 0.0.0.0:8000
