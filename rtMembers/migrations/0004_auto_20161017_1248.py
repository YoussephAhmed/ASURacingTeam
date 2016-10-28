# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rtMembers', '0003_auto_20161017_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rtmember',
            name='userid',
            field=models.OneToOneField(related_name='rtMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
