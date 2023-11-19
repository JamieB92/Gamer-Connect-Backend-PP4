# Generated by Django 3.2.23 on 2023-11-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload',
        ),
        migrations.AddField(
            model_name='post',
            name='upload_clip',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='upload_image',
            field=models.ImageField(blank=True, default='../default_post_ns8zax', upload_to='image/'),
        ),
    ]