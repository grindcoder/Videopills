# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0003_auto_20150403_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 3, 10, 20, 41, 138084)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='videocontainer',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 3, 10, 20, 41, 138960)),
            preserve_default=True,
        ),
    ]
