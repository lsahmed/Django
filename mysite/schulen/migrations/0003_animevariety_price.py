# Generated by Django 5.1.1 on 2024-10-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schulen", "0002_animevariety_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="animevariety",
            name="price",
            field=models.DecimalField(decimal_places=2, default="0", max_digits=5),
        ),
    ]
