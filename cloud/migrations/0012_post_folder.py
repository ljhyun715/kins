# Generated by Django 3.2.8 on 2023-10-13 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0011_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='folder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cloud.folder'),
            preserve_default=False,
        ),
    ]
