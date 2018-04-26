# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('signature', models.CharField(default=b'This guy is too lazy to levave anything here.', max_length=128)),
                ('phone', models.CharField(max_length=11)),
                ('portrait', models.ImageField(default=b'userinfo/initial.jpg.jpg', upload_to=b'userinfo')),
            ],
            options={
                'db_table': 'userinfo',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
