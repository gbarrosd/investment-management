# Generated by Django 4.1 on 2022-08-17 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investments',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.owner', verbose_name='owner'),
        ),
    ]
