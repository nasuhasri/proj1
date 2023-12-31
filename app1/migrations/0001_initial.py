# Generated by Django 4.1 on 2023-06-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Switches",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sw", models.CharField(blank=True, max_length=255, null=True)),
                ("t1", models.IntegerField(blank=True, null=True)),
                ("t2", models.IntegerField(blank=True, null=True)),
                ("t3", models.IntegerField(blank=True, null=True)),
                ("t4", models.IntegerField(blank=True, null=True)),
                ("t5", models.IntegerField(blank=True, null=True)),
                ("ts", models.CharField(blank=True, max_length=255, null=True)),
                ("ts2", models.DateField(blank=True, null=True)),
                ("status", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={"db_table": "switches",},
        ),
    ]
