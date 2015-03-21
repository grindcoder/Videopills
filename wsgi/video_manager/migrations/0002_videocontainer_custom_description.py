# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocontainer',
            name='custom_description',
            field=models.TextField(null=True, max_length=1000),
            preserve_default=True,
        ),
    ]
