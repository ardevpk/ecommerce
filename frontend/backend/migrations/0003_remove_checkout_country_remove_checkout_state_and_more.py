# Generated by Django 4.0.1 on 2022-01-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='country',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='state',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='userName',
        ),
        migrations.AddField(
            model_name='checkout',
            name='aod',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
