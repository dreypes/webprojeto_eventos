# Generated by Django 5.1 on 2024-12-05 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_eventos', '0004_alter_evento_local'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.CharField(max_length=255, verbose_name='Local do Evento'),
        ),
    ]
