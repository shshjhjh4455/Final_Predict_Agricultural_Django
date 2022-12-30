# Generated by Django 4.1 on 2022-12-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_remove_user_area_remove_user_location_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(name="user", options={},),
        migrations.RemoveField(model_name="user", name="date_joined",),
        migrations.RemoveField(model_name="user", name="first_name",),
        migrations.RemoveField(model_name="user", name="groups",),
        migrations.RemoveField(model_name="user", name="is_staff",),
        migrations.RemoveField(model_name="user", name="is_superuser",),
        migrations.RemoveField(model_name="user", name="last_name",),
        migrations.RemoveField(model_name="user", name="user_permissions",),
        migrations.AddField(
            model_name="user",
            name="area",
            field=models.FloatField(default=0, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.CharField(default="서울", max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="user",
            name="nickname",
            field=models.CharField(default="", max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(default="", max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]