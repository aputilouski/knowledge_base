# Generated by Django 3.2.4 on 2021-06-16 13:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='weight',
            field=models.PositiveSmallIntegerField(default=100, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)]),
        ),
    ]