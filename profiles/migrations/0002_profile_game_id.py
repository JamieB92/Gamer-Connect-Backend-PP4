# Generated by Django 3.2.23 on 2023-12-12 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='game_id',
            field=models.IntegerField(null=True),
        ),
    ]
