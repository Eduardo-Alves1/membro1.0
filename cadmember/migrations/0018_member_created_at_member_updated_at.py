# Generated by Django 5.1.7 on 2025-03-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadmember', '0017_alter_member_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='member',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
    ]
