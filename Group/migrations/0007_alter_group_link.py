# Generated by Django 3.2.9 on 2021-12-14 06:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0006_alter_group_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='link',
            field=models.CharField(default='dn67s9sgzhsm1qi', max_length=15, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]