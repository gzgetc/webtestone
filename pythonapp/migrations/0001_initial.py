# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PythonCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('pythoncode', models.TextField()),
                ('time', models.DateTimeField()),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'pythoncourse',
            },
        ),
        migrations.CreateModel(
            name='PythonDirectory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pdnumber', models.CharField(max_length=20)),
                ('pdcontent', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PythonDirectTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('conut', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='pythondirectory',
            name='pdtitle',
            field=models.ForeignKey(to='pythonapp.PythonDirectTitle'),
        ),
        migrations.AddField(
            model_name='pythoncourse',
            name='directory',
            field=models.ForeignKey(to='pythonapp.PythonDirectory'),
        ),
    ]
