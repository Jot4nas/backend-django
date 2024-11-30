# Generated by Django 5.1.3 on 2024-11-30 15:46

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
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=80, unique=True)),
                ("password", models.CharField(max_length=180)),
                ("create_at", models.DateField(auto_now_add=True)),
            ],
        ),
    ]