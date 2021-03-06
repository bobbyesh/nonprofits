# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=256, unique=True)),
                ('associated_name_type', models.CharField(blank=True, max_length=256)),
                ('entity_type', models.CharField(blank=True, max_length=256)),
                ('nonprofit_type', models.CharField(blank=True, max_length=256)),
                ('zip_code', models.IntegerField(null=True)),
                ('address', models.CharField(blank=True, max_length=256)),
                ('city', models.CharField(blank=True, max_length=128)),
                ('registry_number', models.IntegerField(null=True)),
                ('registry_date', models.DateTimeField(null=True)),
                ('state', models.CharField(blank=True, max_length=256)),
                ('latitude', models.DecimalField(decimal_places=9, max_digits=15, null=True)),
                ('longitude', models.DecimalField(decimal_places=9, max_digits=15, null=True)),
            ],
        ),
    ]
