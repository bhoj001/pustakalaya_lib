# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-18 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='type',
            field=models.CharField(default='video', editable=False, max_length=4),
        ),
        migrations.AlterField(
            model_name='video',
            name='date_of_issue',
            field=models.DateField(blank=True, null=True, verbose_name='Date of issue'),
        ),
        migrations.AlterField(
            model_name='video',
            name='year_of_available',
            field=models.DateField(blank=True, null=True, verbose_name='Year of available'),
        ),
    ]