# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Install Node.js 20 (for Tailwind)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# Copy requirements first (for caching)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Set NPM_BIN_PATH for Tailwind
ENV NPM_BIN_PATH=/usr/bin/npm

# Build Tailwind CSS
RUN python manage.py tailwind build

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 10000

# Start Django app using Gunicorn
CMD ["gunicorn", "kamate_group_main.wsgi:application", "--bind", "0.0.0.0:10000"]
