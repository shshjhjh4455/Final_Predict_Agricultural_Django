# Generated by Django 4.1.4 on 2023-01-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recommend", "0002_alter_predictioninput_month"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predictioninput",
            name="month",
            field=models.IntegerField(null=True),
        ),
    ]