# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number_of_bikes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('station_number', models.IntegerField(unique=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('available_docks', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=9, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=9, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Task Name', help_text='select a task to record', max_length=100)),
                ('history', jsonfield.fields.JSONField(verbose_name='history', default={}, help_text='JSON containing the tasks history')),
            ],
            options={
                'verbose_name': 'Task History',
                'verbose_name_plural': 'Task Histories',
            },
        ),
        migrations.CreateModel(
            name='UpdateTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='station',
            field=models.ForeignKey(to_field='station_number', to='api.Station', related_name='bikes'),
        ),
        migrations.AddField(
            model_name='bike',
            name='update',
            field=models.ForeignKey(to='api.UpdateTime', related_name='bike_update'),
        ),
    ]
