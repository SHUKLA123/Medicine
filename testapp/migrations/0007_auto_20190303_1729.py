# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-03 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20190303_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicine', models.CharField(max_length=30)),
                ('Company_Name', models.CharField(max_length=30)),
                ('Number_of_Tablet', models.IntegerField()),
                ('Location', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Pincode', models.IntegerField()),
                ('Phoneno', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sell1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicine', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=30)),
                ('Location', models.CharField(max_length=40)),
                ('Phoneno', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Pincode', models.IntegerField()),
                ('Batch_No', models.CharField(max_length=30)),
                ('Total_Amount', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Buy',
        ),
        migrations.DeleteModel(
            name='Sell',
        ),
    ]
