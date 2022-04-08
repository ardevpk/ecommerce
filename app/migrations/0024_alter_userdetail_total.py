# Generated by Django 4.0.3 on 2022-04-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_recovery_total_userdetail_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=100000000, null=True),
        ),
    ]
