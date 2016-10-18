# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSys', '0007_auto_20161017_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmember',
            name='rtMember',
            field=models.OneToOneField(related_name='ticketMember', to='rtMembers.RTMember'),
        ),
    ]
