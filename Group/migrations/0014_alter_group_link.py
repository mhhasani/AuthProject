# Generated by Django 3.2.9 on 2021-12-15 06:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0013_alter_group_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='link',
            field=models.CharField(default='d4nh4mit34z4lrr', max_length=15, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]