# Generated by Django 5.1.1 on 2025-01-01 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Contact",
            new_name="ContactRequest",
        ),
        migrations.AlterModelOptions(
            name="contactrequest",
            options={
                "verbose_name": "Contact Request",
                "verbose_name_plural": "Contact Requests",
            },
        ),
    ]
