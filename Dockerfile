# 1. Use official Python image
FROM python:3.14-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# 4. Install Node.js (for Tailwind)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm

# 5. Set work directory
WORKDIR /app

# 6. Copy Python requirements
COPY requirements.txt /app/

# 7. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 8. Copy project
COPY . /app/

# 9. Build Tailwind CSS
RUN python manage.py tailwind build

# 10. Collect static files
RUN python manage.py collectstatic --noinput

# 11. Expose port
EXPOSE 8000

# 12. Start server with Gunicorn
CMD ["gunicorn", "kamate_group_main.wsgi:application", "--bind", "0.0.0.0:8000"]
