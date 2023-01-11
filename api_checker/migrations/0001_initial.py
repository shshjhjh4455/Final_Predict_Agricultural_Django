# Generated by Django 4.1 on 2023-01-11 11:31

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
                ("tm", models.IntegerField(default=0)),
                ("pred_5", models.IntegerField()),
                ("pred_10", models.IntegerField()),
                ("pred_20", models.IntegerField()),
                ("pred_60", models.IntegerField()),
                ("pred_120", models.IntegerField()),
            ],
        ),
    ]