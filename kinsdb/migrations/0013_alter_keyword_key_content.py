# Generated by Django 3.2.8 on 2022-08-03 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0012_site_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='key_content',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]