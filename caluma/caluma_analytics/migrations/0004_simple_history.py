# Generated by Django 3.2.13 on 2022-06-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("caluma_analytics", "0003_starting_objects"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalanalyticsfield",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical analytics field",
                "verbose_name_plural": "historical analytics fields",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalanalyticstable",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical analytics table",
                "verbose_name_plural": "historical analytics tables",
            },
        ),
        migrations.AlterField(
            model_name="historicalanalyticsfield",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="historicalanalyticstable",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]
