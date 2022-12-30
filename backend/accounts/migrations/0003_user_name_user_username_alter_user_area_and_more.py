# Generated by Django 4.1.4 on 2022-12-30 07:21

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_area_user_location_user_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Name of User"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(
                default=django.utils.timezone.now,
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="area",
            field=models.CharField(blank=True, max_length=255, verbose_name="Area"),
        ),
        migrations.AlterField(
            model_name="user",
            name="location",
            field=models.CharField(blank=True, max_length=255, verbose_name="Location"),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Phone Number"
            ),
        ),
    ]
