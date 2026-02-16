import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kamate_group_main.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "Kamate20252026"
password = "Kamate@215"
email = "admin@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created.")
else:
    print("Superuser already exists.")
