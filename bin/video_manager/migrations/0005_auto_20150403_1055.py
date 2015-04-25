# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0004_auto_20150403_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='pub_date',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='videocontainer',
            name='pub_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
