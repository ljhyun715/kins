# Generated by Django 3.2.8 on 2023-10-19 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0016_post_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='files',
        ),
    ]
