# Generated by Django 5.0.6 on 2025-01-20 14:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                (
                    "stars",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(
                                5, "O máximo de estrelas é 5"
                            ),
                            django.core.validators.MinValueValidator(
                                0, "O mnínimo de estrelas é 0"
                            ),
                        ],
                    ),
                ),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reviews",
                        to="movies.movie",
                    ),
                ),
            ],
        ),
    ]
