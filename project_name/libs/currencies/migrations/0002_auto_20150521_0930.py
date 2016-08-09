# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currencies'},
        ),
    ]
