# Generated by Django 4.1 on 2022-08-19 01:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investments',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='balance'),
        ),
        migrations.AddField(
            model_name='investments',
            name='income',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='income'),
        ),
        migrations.AddField(
            model_name='investments',
            name='update_date',
            field=models.DateField(blank=True, null=True, verbose_name='updated'),
        ),
    ]
