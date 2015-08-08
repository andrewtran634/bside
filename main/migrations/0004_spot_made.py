# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150807_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='made',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 8, 21, 12, 48, 216000, tzinfo=utc), verbose_name=b'time'),
            preserve_default=False,
        ),
    ]
