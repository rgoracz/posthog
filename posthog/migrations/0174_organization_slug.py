# Generated by Django 3.1.12 on 2021-10-12 15:54

from django.db import IntegrityError, migrations, transaction
from django.utils.text import slugify

from posthog.models.utils import LowercaseSlugField, generate_random_short_suffix

MAX_SLUG_LENGTH = 48


def slugify_all(apps, schema_editor):
    Organization = apps.get_model("posthog", "Organization")
    for instance in Organization.objects.all():
        slugified_name = slugify(instance.name)[:MAX_SLUG_LENGTH]
        for retry_i in range(10):
            # Retry loop to disambiguate possible duplicates. It's EXTREMELY unlikely for the 10 tries to be exhausted
            if not retry_i:
                instance.slug = slugified_name
            else:
                instance.slug = f"{slugified_name[: MAX_SLUG_LENGTH - 5]}-{generate_random_short_suffix()}"
            try:
                with transaction.atomic():
                    instance.save()
            except IntegrityError:
                continue
            else:
                break


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0173_should_update_person_props_function"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="slug",
            field=LowercaseSlugField(max_length=MAX_SLUG_LENGTH, null=True, unique=True),
        ),
        migrations.RunPython(slugify_all, migrations.RunPython.noop, elidable=True),
        migrations.AlterField(
            model_name="organization",
            name="slug",
            field=LowercaseSlugField(max_length=MAX_SLUG_LENGTH, unique=True),
        ),
    ]
