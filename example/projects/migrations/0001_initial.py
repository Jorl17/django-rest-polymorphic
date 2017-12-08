# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-08 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArtProject',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Project')),
                ('artist', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('projects.project',),
        ),
        migrations.CreateModel(
            name='ResearchProject',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Project')),
                ('supervisor', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('projects.project',),
        ),
        migrations.AddField(
            model_name='project',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_projects.project_set+', to='contenttypes.ContentType'),
        ),
    ]