# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtMembers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rtmember',
            name='role',
            field=models.IntegerField(choices=[(0, 'IT'), (1, 'XIT'), (2, 'REC'), (3, 'XREC'), (4, 'OD'), (5, 'XOD'), (6, 'MARK'), (7, 'XMARK'), (8, 'OTHER'), (9, 'XOTHER')]),
        ),
    ]
