# Generated by Django 3.2.8 on 2023-07-28 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0033_test_unique doc'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='docs',
            constraint=models.UniqueConstraint(fields=('document', 'index_num'), name='unique document'),
        ),
    ]
