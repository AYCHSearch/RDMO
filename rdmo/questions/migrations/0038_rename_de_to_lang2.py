# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-29 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0037_rename_en_to_lang1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='title_de',
            new_name='title_lang2',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='help_de',
            new_name='help_lang2',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text_de',
            new_name='text_lang2',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='verbose_name_de',
            new_name='verbose_name_lang2',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='verbose_name_plural_de',
            new_name='verbose_name_plural_lang2',
        ),
        migrations.RenameField(
            model_name='questionset',
            old_name='help_de',
            new_name='help_lang2',
        ),
        migrations.RenameField(
            model_name='questionset',
            old_name='title_de',
            new_name='title_lang2',
        ),
        migrations.RenameField(
            model_name='questionset',
            old_name='verbose_name_de',
            new_name='verbose_name_lang2',
        ),
        migrations.RenameField(
            model_name='questionset',
            old_name='verbose_name_plural_de',
            new_name='verbose_name_plural_lang2',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='title_de',
            new_name='title_lang2',
        ),
    ]
