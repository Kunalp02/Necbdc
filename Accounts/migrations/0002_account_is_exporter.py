# Generated by Django 4.1.3 on 2022-11-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="is_exporter",
            field=models.BooleanField(default=False),
        ),
    ]
