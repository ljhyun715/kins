# Generated by Django 3.2.8 on 2024-01-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0020_alter_files_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='sector',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
