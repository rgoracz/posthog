# Generated by Django 3.2.19 on 2023-11-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0359_team_external_data_workspace_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="externaldatasource",
            name="destination_id",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
