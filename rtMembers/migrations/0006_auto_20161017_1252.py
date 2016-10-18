# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtMembers', '0005_auto_20161017_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rtmember',
            old_name='user',
            new_name='userid',
        ),
    ]
