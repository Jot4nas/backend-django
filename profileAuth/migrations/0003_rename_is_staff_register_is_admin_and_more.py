# Generated by Django 5.1.3 on 2024-11-30 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profileAuth", "0002_register_is_active_register_is_staff_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="register",
            old_name="is_staff",
            new_name="is_admin",
        ),
        migrations.RemoveField(
            model_name="register",
            name="is_superuser",
        ),
    ]
