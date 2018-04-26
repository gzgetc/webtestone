# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('datacode', models.TextField()),
                ('dataimage', models.ImageField(upload_to=b'datacourse')),
                ('time', models.DateTimeField()),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'datacourse',
            },
        ),
        migrations.CreateModel(
            name='DataDirectory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ddnumber', models.CharField(max_length=20)),
                ('ddcontent', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DataDirectTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('conut', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='datadirectory',
            name='ddtitle',
            field=models.ForeignKey(to='databaseapp.DataDirectTitle'),
        ),
        migrations.AddField(
            model_name='datacourse',
            name='directory',
            field=models.ForeignKey(to='databaseapp.DataDirectory'),
        ),
    ]
