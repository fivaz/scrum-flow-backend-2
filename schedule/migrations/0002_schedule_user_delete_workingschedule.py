# Generated by Django 4.2.5 on 2023-09-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("memberId", models.CharField(max_length=255)),
                ("startDate", models.DateField()),
                ("endDate", models.DateField()),
                ("startTime", models.TimeField()),
                ("endTime", models.TimeField()),
                ("daysOfWeek", models.JSONField()),
                ("isRecurring", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cloudId", models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name="WorkingSchedule",
        ),
    ]
