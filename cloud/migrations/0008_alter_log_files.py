# Generated by Django 3.2.8 on 2023-10-05 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0007_auto_20231005_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='files',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.files'),
        ),
    ]
