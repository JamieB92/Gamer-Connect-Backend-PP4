# Generated by Django 3.2.23 on 2023-11-18 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0009_alter_profile_platform_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='platform',
        ),
        migrations.AlterField(
            model_name='profile',
            name='platform_username',
            field=models.CharField(blank=True, max_length=255, verbose_name='Platform Username'),
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gaming_platform', models.CharField(blank=True, choices=[('Xbox', 'Xbox'), ('Playstation', 'Playstation'), ('Steam', 'Steam'), ('Nintendo Switch', 'Nintendo Switch'), ('Discord', 'Discord')], max_length=20, verbose_name='Gaming Platform')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
