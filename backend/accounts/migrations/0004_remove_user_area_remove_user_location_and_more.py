# Generated by Django 4.1.4 on 2022-12-30 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_user_name_user_username_alter_user_area_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="area",
        ),
        migrations.RemoveField(
            model_name="user",
            name="location",
        ),
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
