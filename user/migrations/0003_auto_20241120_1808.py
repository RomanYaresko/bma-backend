# Generated by Django 5.1.3 on 2024-11-20 18:08

from django.db import migrations

def load_initial_data(apps, schema_editor):
    model = apps.get_model('user', 'CustomUser')
    model.objects.create_user(
        username = "admin",
        password = "admin",
        given_name = "Admin User",
        is_staff = True,
    )
    model.objects.create_user(
        username = "casual",
        password = "casual",
        given_name = "Casual User",
        is_staff = False,
    )

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
