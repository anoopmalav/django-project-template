# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('icon', models.ImageField(upload_to='currency')),
                ('code', models.CharField(max_length=10)),
                ('symbol', models.CharField(max_length=100)),
            ],
        ),
    ]
