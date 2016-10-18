# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSys', '0004_auto_20161017_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentimg',
            old_name='commentid',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='ticketcomment',
            old_name='ticketid',
            new_name='ticket',
        ),
        migrations.RenameField(
            model_name='ticketimg',
            old_name='ticketid',
            new_name='ticket',
        ),
    ]
