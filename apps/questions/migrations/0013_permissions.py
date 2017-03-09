# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_meta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'ordering': ('order',), 'permissions': (('view_catalog', 'Can view Catalog'),), 'verbose_name': 'Catalog', 'verbose_name_plural': 'Catalogs'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'permissions': (('view_question', 'Can view Question'),), 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='questionentity',
            options={'ordering': ('subsection__section__catalog__order', 'subsection__section__order', 'subsection__order', 'order'), 'permissions': (('view_questionentity', 'Can view Question entity'),), 'verbose_name': 'Question entity', 'verbose_name_plural': 'Question entities'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('catalog__order', 'order'), 'permissions': (('view_section', 'Can view Section'),), 'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
        migrations.AlterModelOptions(
            name='subsection',
            options={'ordering': ('section__catalog__order', 'section__order', 'order'), 'permissions': (('view_subsection', 'Can view Subsection'),), 'verbose_name': 'Subsection', 'verbose_name_plural': 'Subsections'},
        ),
    ]
