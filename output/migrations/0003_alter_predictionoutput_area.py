# Generated by Django 4.1 on 2023-01-11 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("output", "0002_alter_predictionoutput_area"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predictionoutput",
            name="area",
            field=models.IntegerField(null=True),
        ),
    ]
