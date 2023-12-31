# Generated by Django 3.0.11 on 2021-04-05 19:23

from django.db import migrations


def update_stickiness(apps, schema_editor):
    DashboardItem = apps.get_model("posthog", "DashboardItem")
    for dash in DashboardItem.objects.filter(filters__insight="TRENDS", filters__shown_as="Stickiness"):
        dash.filters["insight"] = "STICKINESS"
        dash.save()


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0146_eventproperty_sync"),
    ]

    operations = [
        migrations.RunPython(update_stickiness, migrations.RunPython.noop, elidable=True),
    ]
