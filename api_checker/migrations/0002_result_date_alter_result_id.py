# Generated by Django 4.1.4 on 2023-01-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_checker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="date",
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="result",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]