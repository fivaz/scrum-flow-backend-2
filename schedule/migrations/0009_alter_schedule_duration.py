# Generated by Django 4.2.5 on 2023-09-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0008_rename_userid_schedule_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="duration",
            field=models.TimeField(blank=True, null=True),
        ),
    ]