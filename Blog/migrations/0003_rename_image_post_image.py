# Generated by Django 4.1.3 on 2022-11-28 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0002_alter_post_comment_postid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="Image",
            new_name="image",
        ),
    ]
