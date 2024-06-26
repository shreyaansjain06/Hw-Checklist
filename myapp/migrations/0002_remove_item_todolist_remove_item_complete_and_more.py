# Generated by Django 5.0.5 on 2024-05-08 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="todolist",
        ),
        migrations.RemoveField(
            model_name="item",
            name="complete",
        ),
        migrations.RemoveField(
            model_name="item",
            name="text",
        ),
        migrations.AddField(
            model_name="item",
            name="c1_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="c1_color",
            field=models.CharField(default="black", max_length=20),
        ),
        migrations.AddField(
            model_name="item",
            name="c2_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="c2_color",
            field=models.CharField(default="black", max_length=20),
        ),
        migrations.AddField(
            model_name="item",
            name="c3_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="c3_color",
            field=models.CharField(default="black", max_length=20),
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                (
                    "Computer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Computer",
                        to="myapp.item",
                    ),
                ),
                (
                    "ELA",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ELA",
                        to="myapp.item",
                    ),
                ),
                (
                    "Gr",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Gr",
                        to="myapp.item",
                    ),
                ),
                (
                    "Language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Language",
                        to="myapp.item",
                    ),
                ),
                (
                    "Math",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Math",
                        to="myapp.item",
                    ),
                ),
                (
                    "Other",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Other",
                        to="myapp.item",
                    ),
                ),
                (
                    "Reading",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Reading",
                        to="myapp.item",
                    ),
                ),
                (
                    "S_S",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="S_S",
                        to="myapp.item",
                    ),
                ),
                (
                    "Sci",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Sci",
                        to="myapp.item",
                    ),
                ),
                (
                    "Test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Test",
                        to="myapp.item",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ToDoList",
        ),
    ]
