# Generated by Django 3.2.8 on 2022-07-04 01:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('charge', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
    ]