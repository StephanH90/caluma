# Generated by Django 3.2.11 on 2022-02-10 09:48

import uuid

import django.contrib.postgres.fields
import django.db.models.deletion
import localized_fields.fields.field
import simple_history.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnalyticsTable",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "created_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "modified_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "modified_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=127, primary_key=True, serialize=False),
                ),
                ("meta", models.JSONField(default=dict)),
                ("disable_visibilities", models.BooleanField(default=False)),
                ("name", localized_fields.fields.field.LocalizedField(required=[])),
                (
                    "starting_object",
                    models.CharField(choices=[("cases", "Cases")], max_length=250),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HistoricalAnalyticsTable",
            fields=[
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "created_at",
                    models.DateTimeField(blank=True, db_index=True, editable=False),
                ),
                (
                    "modified_at",
                    models.DateTimeField(blank=True, db_index=True, editable=False),
                ),
                (
                    "created_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "created_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "modified_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "modified_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                ("slug", models.SlugField(max_length=127)),
                ("meta", models.JSONField(default=dict)),
                ("disable_visibilities", models.BooleanField(default=False)),
                ("name", localized_fields.fields.field.LocalizedField(required=[])),
                (
                    "starting_object",
                    models.CharField(choices=[("cases", "Cases")], max_length=250),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical analytics table",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalAnalyticsField",
            fields=[
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "created_at",
                    models.DateTimeField(blank=True, db_index=True, editable=False),
                ),
                (
                    "modified_at",
                    models.DateTimeField(blank=True, db_index=True, editable=False),
                ),
                (
                    "created_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "created_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "modified_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "modified_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("alias", models.CharField(max_length=100)),
                ("meta", models.JSONField(default=dict)),
                ("data_source", models.TextField()),
                (
                    "filters",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_analytics.analyticstable",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical analytics field",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="AnalyticsField",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "created_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "modified_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "modified_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("alias", models.CharField(max_length=100)),
                ("meta", models.JSONField(default=dict)),
                ("data_source", models.TextField()),
                (
                    "filters",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fields",
                        to="caluma_analytics.analyticstable",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="analyticsfield",
            constraint=models.UniqueConstraint(
                fields=("table", "data_source"), name="unique_data_source"
            ),
        ),
        migrations.AddConstraint(
            model_name="analyticsfield",
            constraint=models.UniqueConstraint(
                fields=("table", "alias"), name="unique_alias"
            ),
        ),
    ]