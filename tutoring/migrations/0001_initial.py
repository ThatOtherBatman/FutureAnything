# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 05:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlueCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=50)),
                ('expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ACT', 'A.C.T.'), ('NSW', 'New South Wales'), ('NT', 'Northern Territory'), ('QLD', 'Queensland'), ('SA', 'South Australia'), ('TAS', 'Tasmania'), ('VIC', 'Victoria'), ('WA', 'Western Australia')], max_length=3)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Strand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('primary_subject', models.BooleanField(default=False)),
                ('secondary_subject', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('subject', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('primary_subject', models.BooleanField(default=False)),
                ('secondary_subject', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TeacherRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=50)),
                ('expiry', models.DateField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.State')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('family_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Gender Non-Binary'), ('X', 'Prefer Not To Say')], max_length=1)),
                ('about', models.TextField()),
                ('abn', models.IntegerField(blank=True, default=None, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('verified', models.CharField(choices=[('N', 'Not Verified'), ('P', 'Pending'), ('V', 'Verified')], default='N', max_length=1)),
            ],
            options={
                'ordering': ('first_name', 'family_name'),
            },
        ),
        migrations.AddField(
            model_name='teacherregistration',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.Tutor'),
        ),
        migrations.AddField(
            model_name='strand',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.Subject'),
        ),
        migrations.AddField(
            model_name='bluecard',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.State'),
        ),
        migrations.AddField(
            model_name='bluecard',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.Tutor'),
        ),
    ]
