# Generated by Django 5.0.6 on 2024-06-21 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadmember', '0004_alter_member_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='date_birth',
            field=models.DateField(default=' ', verbose_name='data_aniversario'),
        ),
        migrations.AddField(
            model_name='member',
            name='city_birth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cidade_nascimento', to='cadmember.city'),
        ),
        migrations.AddField(
            model_name='member',
            name='nationality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nascionalidade', to='cadmember.state'),
        ),
    ]
