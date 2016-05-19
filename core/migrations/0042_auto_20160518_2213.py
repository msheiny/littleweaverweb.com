# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20160518_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'technologies'},
        ),
        migrations.RemoveField(
            model_name='technologysection',
            name='label',
        ),
        migrations.RemoveField(
            model_name='technologysection',
            name='link',
        ),
        migrations.RemoveField(
            model_name='technologysection',
            name='vector',
        ),
        migrations.AlterField(
            model_name='technologysection',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Technology'),
        ),
    ]
