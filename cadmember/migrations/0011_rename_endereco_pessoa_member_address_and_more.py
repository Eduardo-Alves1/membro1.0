# Generated by Django 5.0.6 on 2024-07-10 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadmember', '0010_rename_city_city_cidade_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='endereco_pessoa',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='cep_pessoa',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='cidade_pessoa',
            new_name='city_birth',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='cpf_pessoa',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='batismo_pessoa',
            new_name='date_baptism',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='nascimento_pessoa',
            new_name='date_birth',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='nome_pessoa',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='estado_pessoa',
            new_name='state_birth',
        ),
    ]
