# Generated by Django 3.2.16 on 2023-09-10 07:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="caregory",
            new_name="category",
        ),
    ]
