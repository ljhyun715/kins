# Generated by Django 3.2.8 on 2023-03-08 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0029_alter_issue_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docs',
            old_name='index_title',
            new_name='index_title_kor',
        ),
        migrations.AddField(
            model_name='docs',
            name='index_title_eng',
            field=models.CharField(default='', max_length=100),
        ),
    ]
