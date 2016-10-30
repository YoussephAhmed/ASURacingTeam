# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('foreignClubs', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=1000)),
                ('open', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('year', models.IntegerField()),
                ('attendee_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=1000)),
                ('event', models.ForeignKey(related_name='organize_event', to='events.Event')),
                ('head', models.ForeignKey(related_name='organizer_head', to='foreignClubs.Head')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('max_num', models.IntegerField()),
                ('current_num', models.IntegerField()),
                ('club', models.ForeignKey(related_name='reservation_club', to='foreignClubs.Club')),
                ('event', models.ForeignKey(related_name='reservation_event', to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='organizer',
            name='role',
            field=models.ForeignKey(related_name='organizer_role', to='events.Role'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(related_name='attendee_event', to='events.Event'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(related_name='attendee', to=settings.AUTH_USER_MODEL),
        ),
    ]
