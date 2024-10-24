from django.db import models
from django.utils import timezone #-> Imported to enable the timezone field.

# Create your models here.
class AnimeVariety(models.Model):
    Anime_types = [
        ('JK', 'JUJUTSUKAISEN'),
        ('NR', 'NARUTO'),
        ('AO', 'ATTACKONTITAN'),
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='animeimg/')
    date_added = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=Anime_types)

    def __str__(self):
        return self.name

