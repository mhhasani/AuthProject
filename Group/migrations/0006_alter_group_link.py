# Generated by Django 3.2.9 on 2021-12-14 06:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0005_alter_group_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='link',
            field=models.CharField(default='f1x3zqdm2536257', max_length=15, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
