# Generated by Django 3.2.9 on 2021-12-15 07:55

import AuthApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0013_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(null=True, upload_to=AuthApp.models.path_and_rename),
        ),
    ]
