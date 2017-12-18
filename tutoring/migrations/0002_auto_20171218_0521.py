# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(choices=[('ACT', 'A.C.T.'), ('NSW', 'New South Wales'), ('NT', 'Northern Territory'), ('QLD', 'Queensland'), ('SA', 'South Australia'), ('TAS', 'Tasmania'), ('VIC', 'Victoria'), ('WA', 'Western Australia')], max_length=3, unique=True),
        ),
    ]