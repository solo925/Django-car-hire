# Generated by Django 3.2.19 on 2024-04-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_rename_photo_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
