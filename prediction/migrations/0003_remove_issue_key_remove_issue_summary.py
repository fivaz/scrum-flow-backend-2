# Generated by Django 4.2.5 on 2023-09-23 19:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("prediction", "0002_alter_issue_estimation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="issue",
            name="key",
        ),
        migrations.RemoveField(
            model_name="issue",
            name="summary",
        ),
    ]