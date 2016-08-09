# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=15)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(to='regions.Country', related_name='states')),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='regions.Country', related_name='cities'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='regions.State', related_name='cities'),
        ),
    ]
