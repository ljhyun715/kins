# Generated by Django 3.2.8 on 2023-02-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0020_delete_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docs',
            old_name='content',
            new_name='content_eng',
        ),
        migrations.AddField(
            model_name='docs',
            name='content_kor',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]