# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Common',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CommonIntString',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='propiedades.Common', primary_key=True, serialize=False)),
                ('default', models.CharField(max_length=200)),
                ('mandatory', models.BooleanField()),
            ],
            bases=('propiedades.common',),
        ),
        migrations.CreateModel(
            name='Enum',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='propiedades.Common', primary_key=True, serialize=False)),
                ('key', models.IntegerField(unique=True)),
                ('value', models.CharField(max_length=200)),
            ],
            bases=('propiedades.common',),
        ),
        migrations.CreateModel(
            name='Integer',
            fields=[
                ('commonintstring_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='propiedades.CommonIntString', primary_key=True, serialize=False)),
                ('min', models.BigIntegerField()),
                ('max', models.BigIntegerField()),
            ],
            bases=('propiedades.commonintstring',),
        ),
        migrations.CreateModel(
            name='String',
            fields=[
                ('commonintstring_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='propiedades.CommonIntString', primary_key=True, serialize=False)),
                ('length', models.PositiveIntegerField()),
            ],
            bases=('propiedades.commonintstring',),
        ),
    ]
