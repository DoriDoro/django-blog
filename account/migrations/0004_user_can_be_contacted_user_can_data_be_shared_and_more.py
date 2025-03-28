# Generated by Django 5.1.1 on 2025-01-05 22:08

import account.models
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_profession_service_website_user_professions_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="can_be_contacted",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="can_data_be_shared",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to=account.models._user_directory_path
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="introduction",
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
