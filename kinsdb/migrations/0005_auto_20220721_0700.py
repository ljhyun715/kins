# Generated by Django 3.2.8 on 2022-07-21 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0004_auto_20220721_0650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docs',
            options={'verbose_name': 'Docs', 'verbose_name_plural': 'Docs'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Documents', 'verbose_name_plural': 'Documents'},
        ),
    ]
