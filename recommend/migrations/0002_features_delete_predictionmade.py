# Generated by Django 4.1 on 2023-01-05 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recommend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Features",
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
                ("avr_top", models.FloatField()),
                ("max_top", models.FloatField()),
                ("min_top", models.FloatField()),
                ("rain_top", models.FloatField()),
                ("sun_top", models.FloatField()),
                ("avr_mid", models.FloatField()),
                ("max_mid", models.FloatField()),
                ("min_mid", models.FloatField()),
                ("rain_mid", models.FloatField()),
                ("sun_mid", models.FloatField()),
                ("avr_bot", models.FloatField()),
                ("max_bot", models.FloatField()),
                ("min_bot", models.FloatField()),
                ("rain_bot", models.FloatField()),
                ("sun_bot", models.FloatField()),
            ],
        ),
        migrations.DeleteModel(name="PredictionMade",),
    ]
