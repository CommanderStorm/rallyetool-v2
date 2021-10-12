# Generated by Django 3.2.7 on 2021-10-12 15:57

from django.db import migrations, models


def renamed_station_description(apps, _):
    Station = apps.get_model("ratings", "station")
    for station in Station.objects.all():
        station.location_description = station.description
        station.save()


class Migration(migrations.Migration):
    dependencies = [
        ("ratings", "0005_alter_group_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="station",
            name="latitude",
            field=models.FloatField(
                default=48.265,
                help_text="Visible on the map",
                verbose_name="Latitude of the sation",
            ),
        ),
        migrations.AddField(
            model_name="station",
            name="location_description",
            field=models.CharField(
                default="Location unknown",
                help_text="Visible on the map",
                max_length=500,
                verbose_name="Description of the Station",
            ),
        ),
        migrations.AddField(
            model_name="station",
            name="longitude",
            field=models.FloatField(
                default=11.671,
                help_text="Visible on the map",
                verbose_name="Longitude of the sation",
            ),
        ),
        migrations.AlterField(
            model_name="station",
            name="name",
            field=models.CharField(help_text="Visible on the map", max_length=150, verbose_name="Name of the Station"),
        ),
        migrations.RunPython(renamed_station_description),
        migrations.RemoveField(
            model_name="station",
            name="description",
        ),
    ]