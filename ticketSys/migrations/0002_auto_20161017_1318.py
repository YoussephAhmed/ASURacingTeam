# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='userid',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='state',
            field=models.IntegerField(choices=[(0, 'WAITING_HR'), (1, 'WAITING_IT'), (2, 'WAITING'), (3, 'SOLVED')]),
        ),
        migrations.AlterField(
            model_name='ticketmember',
            name='memberid',
            field=models.OneToOneField(to='rtMembers.RTMember'),
        ),
    ]
