# Generated by Django 5.0.6 on 2024-06-25 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadmember', '0006_remove_member_nationality_member_state_birth_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='date_birth',
            new_name='Data Nascimento',
        ),
    ]
