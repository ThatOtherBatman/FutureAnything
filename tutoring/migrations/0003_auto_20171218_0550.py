# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring', '0002_auto_20171218_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('family_name', models.CharField(max_length=100)),
                ('year', models.CharField(choices=[('K', 'Kindergarten'), ('1', 'Year 1'), ('2', 'Year 2'), ('3', 'Year 3'), ('4', 'Year 4'), ('5', 'Year 5'), ('6', 'Year 6'), ('7', 'Year 7'), ('8', 'Year 8'), ('9', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11'), ('12', 'Year 12')], max_length=2)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'ordering': ('first_name', 'family_name'),
            },
        ),
        migrations.AlterField(
            model_name='tutor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='mobile',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
