# Generated by Django 3.2.9 on 2021-12-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0004_remove_group_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='role',
            field=models.CharField(choices=[('O', 'Owner'), ('A', 'Admin'), ('M', 'Member')], max_length=6, null=True),
        ),
    ]
