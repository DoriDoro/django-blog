# Generated by Django 5.1.1 on 2025-01-05 22:08

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0002_rename_contact_contactrequest_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactrequest",
            name="message",
            field=tinymce.models.HTMLField(),
        ),
    ]
