# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-03 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Searchbar3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=30)),
                ('Nameofperson', models.CharField(max_length=30)),
                ('Location', models.CharField(max_length=30)),
                ('Phoneno', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('Batch_No', models.CharField(max_length=30)),
                ('Total_Amount', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Searchbar2',
        ),
    ]
