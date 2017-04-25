# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=48)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.Cities'),
        ),
    ]