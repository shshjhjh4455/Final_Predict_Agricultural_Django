# Generated by Django 4.1.4 on 2023-01-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_checker", "0003_alter_result_area"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="area",
            field=models.IntegerField(default=0),
        ),
    ]
