# Generated by Django 3.2.8 on 2024-01-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0021_folder_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sector',
        ),
        migrations.AlterField(
            model_name='folder',
            name='sector',
            field=models.CharField(choices=[('1', '기관 제출 공문'), ('2', '참여기관 공유'), ('3', '회의일정 및 전체자료'), ('4', '기타')], default='기타', max_length=100),
        ),
    ]