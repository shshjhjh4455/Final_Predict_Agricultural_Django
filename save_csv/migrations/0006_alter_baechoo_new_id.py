# Generated by Django 4.1.4 on 2023-01-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("save_csv", "0005_alter_baechoo_new_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baechoo_new",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
