# Generated by Django 3.2.19 on 2024-04-24 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_car_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='photo',
            new_name='image',
        ),
    ]