# Generated by Django 3.1.8 on 2021-08-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0161_property_defs_search"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="is_member_join_email_enabled",
            field=models.BooleanField(default=True),
        ),
    ]
