# Generated by Django 4.1.3 on 2022-12-18 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0004_project"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Project",
        ),
    ]
