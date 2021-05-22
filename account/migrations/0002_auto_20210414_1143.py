# Generated by Django 3.1.7 on 2021-04-14 09:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_img',
            field=models.ImageField(default='media/profile_img/doc.png', upload_to='profile_img', verbose_name='profile img'),
        ),
        migrations.AlterField(
            model_name='account',
            name='uid',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('9a349501-c0db-49e0-a685-f8fe668e8a3b'), unique=True, unique_for_date=True),
        ),
    ]
