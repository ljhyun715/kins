# Generated by Django 3.2.8 on 2023-03-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0023_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
