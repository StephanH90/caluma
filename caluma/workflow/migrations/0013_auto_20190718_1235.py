# Generated by Django 2.2.3 on 2019-07-18 12:35

import caluma.core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "workflow",
            "0012_historicalcase_historicalflow_historicaltask_historicaltaskflow_historicalworkflow_historicalworkite",
        )
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="status",
            field=caluma.core.models.ChoicesCharField(
                choices=[
                    ("running", "Case is running and work items need to be completed."),
                    ("completed", "Case is done."),
                    ("canceled", "Case is cancelled."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcase",
            name="status",
            field=caluma.core.models.ChoicesCharField(
                choices=[
                    ("running", "Case is running and work items need to be completed."),
                    ("completed", "Case is done."),
                    ("canceled", "Case is cancelled."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicaltask",
            name="type",
            field=caluma.core.models.ChoicesCharField(
                choices=[
                    ("simple", "Task which can simply be marked as completed."),
                    (
                        "complete_workflow_form",
                        "Task to complete a defined workflow form.",
                    ),
                    ("complete_task_form", "Task to complete a defined task form."),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalworkitem",
            name="status",
            field=caluma.core.models.ChoicesCharField(
                choices=[
                    ("ready", "Task is ready to be processed."),
                    ("completed", "Task is done."),
                    ("canceled", "Task is cancelled."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="type",
            field=caluma.core.models.ChoicesCharField(
                choices=[
                    ("simple", "Task which can simply be marked as completed."),
                    (
                        "complete_workflow_form",
                        "Task to complete a defined workflow form.",
                    ),
                    ("complete_task_form", "Task to complete a defined task form."),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="workitem",
            name="status",
            field=caluma.core.models.ChoicesCharField(
                choices=[
                    ("ready", "Task is ready to be processed."),
                    ("completed", "Task is done."),
                    ("canceled", "Task is cancelled."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
    ]