# Generated by Django 4.1 on 2022-08-28 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("expiry_date", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="Resources",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.IntegerField(unique=True)),
                ("available", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "resources",
            },
        ),
        migrations.CreateModel(
            name="ResourceScheduling",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("initial_date", models.DateTimeField()),
                ("final_date", models.DateTimeField()),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="gerenciador.resources",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "resource_scheduling",
            },
        ),
    ]
