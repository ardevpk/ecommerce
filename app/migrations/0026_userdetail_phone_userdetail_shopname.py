# Generated by Django 4.0.3 on 2022-04-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_returns_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='phone',
            field=models.CharField(blank=True, default='+923000000000', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='shopname',
            field=models.CharField(blank=True, default='Your Electronics Shop', max_length=254, null=True),
        ),
    ]