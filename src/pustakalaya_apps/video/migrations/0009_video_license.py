# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-12 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180312_1353'),
        ('video', '0008_merge_20180312_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='license',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.LicenseType', verbose_name='license'),
        ),
    ]
