# Generated by Django 5.1.7 on 2025-03-18 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadmember', '0014_rename_cidade_city_city_rename_estado_state_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='cpf',
            field=models.CharField(max_length=11, null=True, unique=True, verbose_name='cpf'),
        ),
    ]
