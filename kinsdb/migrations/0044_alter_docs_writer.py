# Generated by Django 3.2.8 on 2023-08-24 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kinsdb', '0043_document_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='writer',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
