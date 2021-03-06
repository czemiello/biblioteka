# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-09 11:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('stanowisko', models.CharField(max_length=150)),
                ('kod_pocztowy', models.CharField(max_length=6)),
                ('nr_tel', models.CharField(max_length=12)),
                ('miasto', models.CharField(max_length=250)),
                ('nr_domu', models.CharField(max_length=10)),
                ('nr_lokalu', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='siteuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
