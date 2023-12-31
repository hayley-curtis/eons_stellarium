# Generated by Django 4.1.7 on 2023-05-10 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("asterisms", "0002_continent_region_alter_culture_geographic_region"),
    ]

    operations = [
        migrations.AlterField(
            model_name="culture",
            name="geographic_region",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="asterisms.region",
            ),
        ),
    ]
