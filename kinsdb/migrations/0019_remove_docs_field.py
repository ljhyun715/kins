# Generated by Django 3.2.8 on 2023-01-18 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0018_docs_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docs',
            name='field',
        ),
    ]
