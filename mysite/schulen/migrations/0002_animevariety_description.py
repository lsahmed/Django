# Generated by Django 5.1.1 on 2024-10-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schulen", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animevariety",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
