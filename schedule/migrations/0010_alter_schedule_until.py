# Generated by Django 4.2.5 on 2023-09-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0009_alter_schedule_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="until",
            field=models.DateField(blank=True, null=True),
        ),
    ]
