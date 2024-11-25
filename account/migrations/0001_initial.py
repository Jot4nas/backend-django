# Generated by Django 5.1.3 on 2024-11-24 16:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Register",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=80)),
                ("password", models.CharField(max_length=180)),
                ("create_at", models.DateField(auto_now_add=True)),
            ],
        ),
    ]