# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadCaption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identification', models.CharField(max_length=10)),
                ('maxtitle', models.CharField(max_length=50)),
                ('mintitle', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'headcaption',
            },
        ),
        migrations.CreateModel(
            name='PhotoDescrib',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'photodescrib')),
                ('imgorder', models.IntegerField()),
                ('imgname', models.CharField(max_length=50)),
                ('texttitle', models.CharField(max_length=50)),
                ('textcontent', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'photodescrib',
            },
        ),
        migrations.CreateModel(
            name='PhotoLbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'photolbum')),
                ('imgorder', models.IntegerField()),
                ('imgname', models.CharField(max_length=50)),
                ('imgtitle', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'photolbum',
            },
        ),
    ]
