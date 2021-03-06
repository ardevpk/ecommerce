# Generated by Django 4.0.1 on 2022-01-30 14:59

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eCompOrders', models.IntegerField()),
                ('eTakenProdPrice', models.IntegerField()),
                ('eRecievenCash', models.IntegerField()),
                ('ename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('tag', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=10000)),
                ('color', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=500)),
                ('image', models.ImageField(default='https://via.placeholder.com/550x750', upload_to='uploads/')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
        ),
        migrations.CreateModel(
            name='returns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rByName', models.CharField(max_length=500)),
                ('rByPhone', models.IntegerField()),
                ('rByAddress', models.CharField(max_length=500)),
                ('rOrderPrice', models.IntegerField()),
                ('rOrderProdDetail', models.CharField(max_length=10000)),
                ('rOnDate', models.DateField(auto_now_add=True)),
                ('rTakenBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.employee')),
            ],
        ),
        migrations.CreateModel(
            name='recovery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recPrice', models.IntegerField()),
                ('rOnDate', models.DateField(auto_now_add=True)),
                ('recByName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.employee')),
                ('recByWhichShop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='eRecievenCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eRDate', models.DateField(auto_now_add=True)),
                ('eRname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.employee')),
            ],
        ),
        migrations.CreateModel(
            name='cOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderByPhone', models.IntegerField()),
                ('orderByAddress', models.CharField(max_length=500)),
                ('cOnDate', models.DateField(auto_now_add=True)),
                ('cOrderPrice', models.IntegerField()),
                ('cOrderProdName', models.CharField(max_length=500)),
                ('cOrderProdQuan', models.CharField(max_length=500)),
                ('cOrderProdId', models.CharField(max_length=500)),
                ('cBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.employee')),
                ('orderByName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clShopName', models.CharField(max_length=500)),
                ('clShopAddress', models.CharField(max_length=500)),
                ('clPhone', models.IntegerField()),
                ('clPendingBalance', models.IntegerField()),
                ('clPaidBalance', models.IntegerField()),
                ('clOnCredit', models.BooleanField(default=False)),
                ('clName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.CharField(max_length=500)),
                ('shopName', models.CharField(max_length=500)),
                ('userName', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('country', models.CharField(default='pakistan', max_length=500)),
                ('state', models.CharField(default='lahore', max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('toPay', models.IntegerField()),
                ('checkoutProdId', models.CharField(max_length=1000)),
                ('checkoutProdName', models.CharField(max_length=10000)),
                ('checkoutProdQuan', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
                ('checkoutName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodId', models.IntegerField()),
                ('prodPrice', models.IntegerField()),
                ('prodTag', models.CharField(max_length=5000)),
                ('prodName', models.CharField(max_length=5000)),
                ('prodBrand', models.CharField(max_length=5000)),
                ('prodImage', models.CharField(default='https://via.placeholder.com/100x100', max_length=5000)),
                ('prodQuan', models.IntegerField()),
                ('perProdTotal', models.IntegerField()),
                ('cartName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
