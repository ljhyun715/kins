# Generated by Django 3.2.8 on 2023-08-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0039_alter_data_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='wc',
            field=models.ImageField(blank=True, null=True, upload_to='data'),
        ),
    ]
