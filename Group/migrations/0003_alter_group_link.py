# Generated by Django 3.2.9 on 2021-12-12 08:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0002_alter_group_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='link',
            field=models.CharField(default='nfi88xxxgh5cshy', max_length=15, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
