# Generated by Django 4.0.3 on 2022-03-30 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_order_total_order_percent_order_save_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='save',
            new_name='saved',
        ),
    ]