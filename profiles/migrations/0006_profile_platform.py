# Generated by Django 3.2.23 on 2023-11-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_user_profile_profile_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='platform',
            field=models.CharField(blank=True, choices=[('Xbox', 'Xbox'), ('Playstation', 'Playstation'), ('Steam', 'Steam'), ('Nintendo Switch', 'Nintendo Switch'), ('Discord', 'Discord')], max_length=20, verbose_name='Preferred'),
        ),
    ]
