# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-03 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180503_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='authors_name_in_other_language',
            field=models.ManyToManyField(blank=True, related_name='_biography_authors_name_in_other_language_+', to='core.Biography', verbose_name='Author(s) name in other language'),
        ),
    ]