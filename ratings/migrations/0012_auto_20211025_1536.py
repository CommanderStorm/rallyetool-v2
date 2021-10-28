# Generated by Django 3.2.7 on 2021-10-25 13:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ratings", "0011_auto_20211023_1743"),
    ]

    operations = [
        migrations.CreateModel(
            name="RatingScheme3",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="rating",
            name="handicap",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Needed for the RatingScheme 3",
                null=True,
                verbose_name="Handicap used for grading. (i.e. group-size)",
            ),
        ),
        migrations.AddField(
            model_name="rating",
            name="value",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Needed for the RatingScheme 2 or 3",
                null=True,
                verbose_name="Value achieved by the group",
            ),
        ),
        migrations.AddField(
            model_name="station",
            name="rating_scheme_choices",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "1 - Rating of the groups by the tutors is final. No scheme."),
                    (2, "2 - Rating of the groups by the tutors is based on a single key."),
                    (3, "3 - Rating of the groups by the tutors is based on multiple keys (one for each handicap)."),
                ],
                default=1,
                verbose_name="Rating Scheme",
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="points",
            field=models.IntegerField(
                default=0,
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
            ),
        ),
        migrations.CreateModel(
            name="RatingScheme3Group",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "mark_for_10p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 10 points"),
                ),
                (
                    "mark_for_9p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 9 points"),
                ),
                (
                    "mark_for_8p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 8 points"),
                ),
                (
                    "mark_for_7p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 7 points"),
                ),
                (
                    "mark_for_6p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 6 points"),
                ),
                (
                    "mark_for_5p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 5 points"),
                ),
                (
                    "mark_for_4p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 4 points"),
                ),
                (
                    "mark_for_3p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 3 points"),
                ),
                (
                    "mark_for_2p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 2 points"),
                ),
                (
                    "mark_for_1p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 1 point"),
                ),
                ("handicap", models.PositiveIntegerField(verbose_name="Handicap used for grading. (i.e. group-size)")),
                (
                    "rating_scheme",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="ratings.ratingscheme3"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="ratingscheme3",
            name="station",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="ratings.station"),
        ),
        migrations.CreateModel(
            name="RatingScheme2",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "mark_for_10p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 10 points"),
                ),
                (
                    "mark_for_9p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 9 points"),
                ),
                (
                    "mark_for_8p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 8 points"),
                ),
                (
                    "mark_for_7p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 7 points"),
                ),
                (
                    "mark_for_6p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 6 points"),
                ),
                (
                    "mark_for_5p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 5 points"),
                ),
                (
                    "mark_for_4p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 4 points"),
                ),
                (
                    "mark_for_3p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 3 points"),
                ),
                (
                    "mark_for_2p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 2 points"),
                ),
                (
                    "mark_for_1p",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="Min-value for 1 point"),
                ),
                ("station", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="ratings.station")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RatingScheme1",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("station", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="ratings.station")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
