# Generated by Django 3.2.8 on 2022-08-02 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0008_keyword_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='group',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
