# Generated by Django 4.1.4 on 2023-01-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Result",
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
                ("date", models.DateField()),
                ("pred_5", models.FloatField()),
                ("pred_10", models.FloatField()),
                ("pred_20", models.FloatField()),
                ("pred_60", models.FloatField()),
                ("pred_120", models.FloatField()),
            ],
        ),
    ]
