# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_spot_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='time',
            field=models.FloatField(),
        ),
    ]
