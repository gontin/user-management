# Generated by Django 5.1.5 on 2025-01-31 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_data_situacao_emprego_data_tipo_moradia'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
