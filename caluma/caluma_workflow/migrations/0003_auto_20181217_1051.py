# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-17 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("caluma_workflow", "0002_auto_20181213_1334")]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="type",
            field=models.CharField(
                choices=[
                    ("simple", "Task which can only be marked as completed."),
                    (
                        "complete_workflow_form",
                        "Task completing defined workflow form.",
                    ),
                ],
                max_length=50,
            ),
        )
    ]
