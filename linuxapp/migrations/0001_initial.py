# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinuxCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('linuxcode', models.TextField()),
                ('time', models.DateTimeField()),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'linuxcourse',
            },
        ),
        migrations.CreateModel(
            name='LinuxDirectory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ldnumber', models.CharField(max_length=20)),
                ('ldcontent', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LinuxDirectTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('conut', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='linuxdirectory',
            name='ldtitle',
            field=models.ForeignKey(to='linuxapp.LinuxDirectTitle'),
        ),
        migrations.AddField(
            model_name='linuxcourse',
            name='directory',
            field=models.ForeignKey(to='linuxapp.LinuxDirectory'),
        ),
    ]
