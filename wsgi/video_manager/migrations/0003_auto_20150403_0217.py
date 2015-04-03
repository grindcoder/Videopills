# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0002_videocontainer_custom_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 3, 2, 17, 32, 771683), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videocontainer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 3, 2, 17, 32, 772610), verbose_name='date created'),
            preserve_default=True,
        ),
    ]
