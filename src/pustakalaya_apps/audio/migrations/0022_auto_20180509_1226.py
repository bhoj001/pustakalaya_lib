# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0021_auto_20180509_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_read_by',
            field=models.ManyToManyField(blank=True, related_name='audio_read_by', to='core.Biography', verbose_name='Read / Voice by'),
        ),
    ]