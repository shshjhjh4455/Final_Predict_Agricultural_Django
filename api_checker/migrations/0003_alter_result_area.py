# Generated by Django 4.1.4 on 2023-01-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_checker", "0002_result_area"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="area",
            field=models.IntegerField(),
        ),
    ]