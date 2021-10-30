from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
from django.urls import reverse
import requests


# objects auto populate fields by title search with override save.  
# elif title_id is allows corrective measure by movie number for a movie with wrong title population. 

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=100, default='')
    title_id = models.CharField(blank=True, max_length=10, default='')
    rx_title = models.CharField(blank=True, max_length=100, default='')
    media = models.FileField(upload_to='library', validators=[FileExtensionValidator(['mp4','mkv'])])
    cover = models.CharField(blank=True, max_length=250, default='')
    year = models.CharField(blank=True, max_length=12, default='')
    rating = models.CharField(blank=True, max_length=4, default='')
    plot = models.TextField(blank=True, max_length=1500, default='')
    genre1 = models.CharField(blank=True, max_length=20, default='')
    genre2 = models.CharField(blank=True, max_length=20, default='')
    genre3 = models.CharField(blank=True, max_length=20, default='')
    popularity = models.CharField(blank=True, max_length=10, default='')
    is_published = models.BooleanField(default=True)
    mpaa_rating = models.IntegerField(blank=True, default=0)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    tagline = models.TextField(blank=True, max_length=200, default='')
    actor1 = models.CharField(blank=True, max_length=100, default='')
    actor2 = models.CharField(blank=True, max_length=100, default='')
    actor3 = models.CharField(blank=True, max_length=100, default='')
    actor4 = models.CharField(blank=True, max_length=100, default='')
    actor5 = models.CharField(blank=True, max_length=100, default='')
    actor6 = models.CharField(blank=True, max_length=100, default='')
    budget = models.IntegerField(blank=True, default=0)
    kwords0 = models.CharField(blank=True, max_length=60, default='')
    kwords1 = models.CharField(blank=True, max_length=60, default='')
    kwords2 = models.CharField(blank=True, max_length=60, default='')
    kwords3 = models.CharField(blank=True, max_length=60, default='')
    kwords4 = models.CharField(blank=True, max_length=60, default='')
    kwords5 = models.CharField(blank=True, max_length=60, default='')
    kwords6 = models.CharField(blank=True, max_length=60, default='')
    kwords7 = models.CharField(blank=True, max_length=60, default='')
    kwords8 = models.CharField(blank=True, max_length=60, default='')
    kwords9 = models.CharField(blank=True, max_length=60, default='')
    bonus_tag1 = models.CharField(blank=True, max_length=30, default='')
    bonus_tag2 = models.CharField(blank=True, max_length=30, default='')

    # def save(self, *args, **kwargs):

    def save(self, *args, **kwargs):

        if self.title:

            r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=c81378bff6e0ed65976caaace3ea2306&language=en-US&query={self.title}&page=1&include_adult=false')

            try:
                self.title_id = r.json()['results'][0]['id']
            except:
                self.title_id = ''
            try:
                self.rx_title = r.json()['results'][0]['title']
            except:
                self.rx_title = ''
            try:
                self.cover = r.json()['results'][0]['poster_path']
            except:
                self.cover = '/sH6030EbSzOUTFFZrpnTdSpeNP0.jpg'
            try:
                self.year = r.json()['results'][0]['release_date']
            except:
                self.year = ''
            try:
                self.rating = r.json()['results'][0]['vote_average']
            except:
                self.rating = ''
            try:
                self.plot = r.json()['results'][0]['overview']
            except:
                self.plot = ''
            try:
                self.popularity = r.json()['results'][0]['popularity']
            except:
                self.popularity = ''

            x = requests.get(f'https://api.themoviedb.org/3/movie/{self.title_id}?api_key=c81378bff6e0ed65976caaace3ea2306&language=en-US&append_to_response=credits')

            try:
                self.tagline = x.json()['tagline']
            except:
                self.tagline = ''
            try:
                self.genre1 = x.json()['genres'][0]['name']
            except:
                self.genre1 = ''
            try:
                self.genre2 = x.json()['genres'][1]['name']
            except:
                self.genre2 = ''
            try:
                self.genre3 = x.json()['genres'][2]['name']
            except:
                self.genre3 = ''
            try:
                self.actor1 = x.json()['credits']['cast'][0]['name']
            except:
                self.actor1 = ''
            try:
                self.actor2 = x.json()['credits']['cast'][1]['name']
            except:
                self.actor2 = ''
            try:
                self.actor3 = x.json()['credits']['cast'][2]['name']
            except:
                self.actor3 = ''
            try:
                self.actor4 = x.json()['credits']['cast'][3]['name']
            except:
                self.actor4 = ''
            try:
                self.actor5 = x.json()['credits']['cast'][4]['name']
            except:
                self.actor5 = ''
            try:
                self.actor6 = x.json()['credits']['cast'][5]['name']
            except:
                self.actor6 = ''
            try:
                self.budget = x.json()['budget']
            except:
                self.budget = 0

            x = requests.get(f'https://api.themoviedb.org/3/movie/{self.title_id}/keywords?api_key=c81378bff6e0ed65976caaace3ea2306')

            try:
                self.kwords0 = x.json()['keywords'][0]['name']
            except:
                self.kwords0 = ''
            try:
                self.kwords1 = x.json()['keywords'][1]['name']
            except:
                self.kwords1 = ''
            try:
                self.kwords2 = x.json()['keywords'][2]['name']
            except:
                self.kwords2 = ''
            try:
                self.kwords3 = x.json()['keywords'][3]['name']
            except:
                self.kwords3 = ''
            try:
                self.kwords4 = x.json()['keywords'][4]['name']
            except:
                self.kwords4 = ''
            try:
                self.kwords5 = x.json()['keywords'][5]['name']
            except:
                self.kwords5 = ''
            try:
                self.kwords6 = x.json()['keywords'][6]['name']
            except:
                self.kwords6 = ''
            try:
                self.kwords7 = x.json()['keywords'][7]['name']
            except:
                self.kwords7 = ''
            try:
                self.kwords8 = x.json()['keywords'][8]['name']
            except:
                self.kwords8 = ''
            try:
                self.kwords9 = x.json()['keywords'][9]['name']
            except:
                self.kwords9 = ''

        elif self.title_id:

            x = requests.get(f'https://api.themoviedb.org/3/movie/{self.title_id}?api_key=c81378bff6e0ed65976caaace3ea2306&language=en-US&append_to_response=credits')

            try:
                self.rx_title = x.json()['original_title']
            except:
                self.rx_title = ''
            try:
                self.cover = x.json()['poster_path']
            except:
                self.cover = '/sH6030EbSzOUTFFZrpnTdSpeNP0.jpg'
            try:
                self.year = x.json()['release_date']
            except:
                self.year = ''
            try:
                self.rating = x.json()['vote_average']
            except:
                self.rating = ''
            try:
                self.plot = x.json()['overview']
            except:
                self.plot = ''
            try:
                self.popularity = x.json()['popularity']
            except:
                self.popularity = ''
            try:
                self.tagline = x.json()['tagline']
            except:
                self.tagline = ''
            try:
                self.genre1 = x.json()['genres'][0]['name']
            except:
                self.genre1 = ''
            try:
                self.genre2 = x.json()['genres'][1]['name']
            except:
                self.genre2 = ''
            try:
                self.genre3 = x.json()['genres'][2]['name']
            except:
                self.genre3 = ''
            try:
                self.actor1 = x.json()['credits']['cast'][0]['name']
            except:
                self.actor1 = ''
            try:
                self.actor2 = x.json()['credits']['cast'][1]['name']
            except:
                self.actor2 = ''
            try:
                self.actor3 = x.json()['credits']['cast'][2]['name']
            except:
                self.actor3 = ''
            try:
                self.actor4 = x.json()['credits']['cast'][3]['name']
            except:
                self.actor4 = ''
            try:
                self.actor5 = x.json()['credits']['cast'][4]['name']
            except:
                self.actor5 = ''
            try:
                self.actor6 = x.json()['credits']['cast'][5]['name']
            except:
                self.actor6 = ''
            try:
                self.budget = x.json()['budget']
            except:
                self.budget = 0

            x = requests.get(f'https://api.themoviedb.org/3/movie/{self.title_id}/keywords?api_key=c81378bff6e0ed65976caaace3ea2306')

            try:
                self.kwords0 = x.json()['keywords'][0]['name']
            except:
                self.kwords0 = ''
            try:
                self.kwords1 = x.json()['keywords'][1]['name']
            except:
                self.kwords1 = ''
            try:
                self.kwords2 = x.json()['keywords'][2]['name']
            except:
                self.kwords2 = ''
            try:
                self.kwords3 = x.json()['keywords'][3]['name']
            except:
                self.kwords3 = ''
            try:
                self.kwords4 = x.json()['keywords'][4]['name']
            except:
                self.kwords4 = ''
            try:
                self.kwords5 = x.json()['keywords'][5]['name']
            except:
                self.kwords5 = ''
            try:
                self.kwords6 = x.json()['keywords'][6]['name']
            except:
                self.kwords6 = ''
            try:
                self.kwords7 = x.json()['keywords'][7]['name']
            except:
                self.kwords7 = ''
            try:
                self.kwords8 = x.json()['keywords'][8]['name']
            except:
                self.kwords8 = ''
            try:
                self.kwords9 = x.json()['keywords'][9]['name']
            except:
                self.kwords9 = ''


        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('video', args=[str(self.id)])
