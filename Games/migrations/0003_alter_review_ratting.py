# Generated by Django 3.2.9 on 2021-12-07 08:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0002_rename_reviews_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ratting',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
