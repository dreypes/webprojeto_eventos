# Generated by Django 5.1 on 2024-12-05 03:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_eventos', '0006_remove_evento_criador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='convite',
            name='convidado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='convite',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eventos.evento'),
        ),
        migrations.AlterField(
            model_name='convite',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('aceito', 'Aceito'), ('recusado', 'Recusado')], default='pendente', max_length=10),
        ),
    ]