from django.db import models
from django.utils import timezone #-> Imported to enable the timezone field.
from django.contrib.auth.models import User

# Create your models here.
class AnimeVariety(models.Model):
    Anime_types = [
        ('LS', 'LONGSEASONS'),
        ('MP', 'MASTERPIECE'),
        ('AT', 'ACTIONTHRILLER'),
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='animeimg/')
    date_added = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=Anime_types)
    price = models.DecimalField(max_digits=5, decimal_places=2, default='0')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    
# one to many

class AnimeReview(models.Model):
    anime = models.ForeignKey(AnimeVariety, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default='')
    comment = models.TextField()
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.anime.name}"
    
# many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    anime_varities = models.ManyToManyField(AnimeVariety, related_name='stores')

    def __str__(self):
        return self.name
    
# One to One
class AnimeCertificate(models.Model):
    anime = models.OneToOneField(AnimeVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)
    valid_until = models.DateField()

    def __str__(self):
        return f"Certificate for {self.anime.name}"

class AnimeUA(models.Model):
    animeua = models.ForeignKey(AnimeVariety, on_delete=models.CASCADE, null=True, related_name='ua_rating')
    age_certification = models.IntegerField(default='')
    def __str__(self):
        return f"UA Certification for {self.animeua.name}"

