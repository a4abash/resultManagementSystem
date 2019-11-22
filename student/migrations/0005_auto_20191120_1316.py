# Generated by Django 2.2.4 on 2019-11-20 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20191120_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='rts',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='result',
            name='se',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)]),
        ),
    ]
