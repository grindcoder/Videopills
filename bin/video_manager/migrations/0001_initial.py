# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('series_name', models.CharField(max_length=50)),
                ('episode_trailer', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoContainer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('episode_trailer_filename', models.CharField(max_length=100)),
                ('episode_name', models.ForeignKey(to='video_manager.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
