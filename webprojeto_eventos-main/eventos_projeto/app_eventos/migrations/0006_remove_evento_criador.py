# Generated by Django 5.1 on 2024-12-05 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eventos', '0005_alter_evento_local'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='criador',
        ),
    ]
