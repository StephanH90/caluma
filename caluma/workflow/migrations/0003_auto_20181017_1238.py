# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("workflow", "0002_auto_20181009_1108")]

    operations = [
        migrations.RenameField(
            model_name="case", old_name="created", new_name="created_at"
        ),
        migrations.RenameField(
            model_name="case", old_name="modified", new_name="modified_at"
        ),
        migrations.RenameField(
            model_name="flow", old_name="created", new_name="created_at"
        ),
        migrations.RenameField(
            model_name="flow", old_name="modified", new_name="modified_at"
        ),
        migrations.RenameField(
            model_name="task", old_name="created", new_name="created_at"
        ),
        migrations.RenameField(
            model_name="task", old_name="modified", new_name="modified_at"
        ),
        migrations.RenameField(
            model_name="workflow", old_name="created", new_name="created_at"
        ),
        migrations.RenameField(
            model_name="workflow", old_name="modified", new_name="modified_at"
        ),
        migrations.RenameField(
            model_name="workitem", old_name="created", new_name="created_at"
        ),
        migrations.RenameField(
            model_name="workitem", old_name="modified", new_name="modified_at"
        ),
        migrations.AddField(
            model_name="case",
            name="created_by_group",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="case",
            name="created_by_user",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="flow",
            name="created_by_group",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="flow",
            name="created_by_user",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="created_by_group",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="created_by_user",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="workflow",
            name="created_by_group",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="workflow",
            name="created_by_user",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="workitem",
            name="created_by_group",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="workitem",
            name="created_by_user",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]