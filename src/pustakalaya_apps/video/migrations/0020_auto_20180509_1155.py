# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 06:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0019_auto_20180420_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videofileupload',
            options={'ordering': ['created_date']},
        ),
        migrations.AlterModelOptions(
            name='videolinkinfo',
            options={'ordering': ['created_date']},
        ),
        migrations.AlterModelOptions(
            name='videoseries',
            options={'ordering': ['created_date'], 'verbose_name_plural': 'Video series'},
        ),
    ]
