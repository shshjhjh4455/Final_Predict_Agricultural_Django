# Generated by Django 4.1 on 2023-01-02 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_user_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(default="", max_length=100),
        ),
    ]
