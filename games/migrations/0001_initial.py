# Generated by Django 3.2.23 on 2023-12-11 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('looking_for_friends', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'Yes')], max_length=20, verbose_name='Looking For Friends')),
                ('experience', models.CharField(blank=True, choices=[('Noob', 'Noob'), ('Casual', 'Casual'), ('Pro', 'Pro'), ('Vetran', 'Vetran'), ('Master', 'Master'), ('God', 'God')], max_length=20, verbose_name='Looking For Friends')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='profiles.profile')),
            ],
        ),
    ]
