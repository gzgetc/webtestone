# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JavaCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('javacode', models.TextField()),
                ('time', models.DateTimeField()),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'javacourse',
            },
        ),
        migrations.CreateModel(
            name='JavaDirectory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jdnumber', models.CharField(max_length=20)),
                ('jdcontent', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JavaDirectTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('conut', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='javadirectory',
            name='jdtitle',
            field=models.ForeignKey(to='javaapp.JavaDirectTitle'),
        ),
        migrations.AddField(
            model_name='javacourse',
            name='directory',
            field=models.ForeignKey(to='javaapp.JavaDirectory'),
        ),
    ]
