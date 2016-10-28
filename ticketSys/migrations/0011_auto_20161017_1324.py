# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSys', '0010_auto_20161017_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketcomment',
            old_name='member',
            new_name='ticketMember',
        ),
    ]
