# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Html5Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('html5code', models.TextField()),
                ('html5image', models.ImageField(upload_to=b'html5course')),
                ('time', models.DateTimeField()),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'html5course',
            },
        ),
        migrations.CreateModel(
            name='Html5Directory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hdnumber', models.CharField(max_length=20)),
                ('hdcontent', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'html5directory',
            },
        ),
        migrations.CreateModel(
            name='Html5DirectTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('conut', models.IntegerField()),
            ],
            options={
                'db_table': 'html5directtitle',
            },
        ),
        migrations.AddField(
            model_name='html5directory',
            name='hdtitle',
            field=models.ForeignKey(to='html5app.Html5DirectTitle'),
        ),
        migrations.AddField(
            model_name='html5course',
            name='directory',
            field=models.ForeignKey(to='html5app.Html5Directory'),
        ),
    ]
