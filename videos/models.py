from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
from django.urls import reverse
import requests

class Video(models.Model):    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    rx_title = models.CharField(blank=True, max_length=100)
    media = models.FileField(upload_to='library', validators=[FileExtensionValidator(['mp4','mkv'])])
    cover = models.CharField(blank=True, max_length=250)
    year = models.CharField(blank=True, max_length=12)
    rating = models.CharField(blank=True, max_length=4)
    plot = models.TextField(blank=True, max_length=1500)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=c81378bff6e0ed65976caaace3ea2306&language=en-US&query={self.title}&page=1&include_adult=false')
        self.rx_title = r.json()['results'][0]['title']
        self.cover = r.json()['results'][0]['poster_path']
        self.year = r.json()['results'][0]['release_date']
        self.rating = r.json()['results'][0]['vote_average']
        self.plot = r.json()['results'][0]['overview']

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('video', args=[str(self.id)])

# api_key= is demo. Get a new key from TMDB