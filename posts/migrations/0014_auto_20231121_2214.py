# Generated by Django 3.2.23 on 2023-11-21 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_alter_post_upload_clip'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='uploaded_on',
            new_name='created_at',
        ),
    ]