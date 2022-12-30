# Generated by Django 4.1.4 on 2022-12-30 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="area",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                default=django.utils.timezone.now, max_length=10, unique=True
            ),
            preserve_default=False,
        ),
    ]
