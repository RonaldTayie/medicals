# Generated by Django 3.1.7 on 2021-05-28 01:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210528_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lid',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('ca62a5ca-d69a-4b9a-84b9-94821853c2d7'), unique=True, unique_for_date=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_code',
            field=models.CharField(default='StCd', max_length=8),
        ),
    ]