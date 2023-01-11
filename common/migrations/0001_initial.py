# Generated by Django 4.1 on 2023-01-11 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("phone", models.CharField(max_length=20, null=True)),
                ("area", models.CharField(max_length=20, null=True)),
                ("location", models.CharField(max_length=20, null=True)),
                ("month", models.IntegerField(null=True)),
            ],
        ),
    ]
