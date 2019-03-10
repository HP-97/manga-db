from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from common.util import mangaScrape
import datetime

"""
References:

Foreign Key Django Model
https://stackoverflow.com/questions/14663523/foreign-key-django-model

Movie Database, storing multiple genres
https://stackoverflow.com/questions/17520720/movie-database-storing-multiple-genres/17520721
"""

# Create your models here.
class MangaManager(models.Manager):
	def add_manga(self, url_chapter, url_metadata):
		# Insert manga information
		scraped_data = mangaScrape.retrieve_data(url_chapter, url_metadata)
		date_uploaded = datetime.strptime(scraped_data['date uploaded'], '%d/%m/%Y')
		release_date = datetime.strptime(scraped_data['release date'], '%b %d, %Y')
		data_manga = {
			'title': scraped_data['title'],
			'author': scraped_data['author'],
			'pub_status': scraped_data['pub status'],
			'latest_chapter': scraped_data['latest chapter'],
			'date_uploaded': date_uploaded,
			'release_date': release_date,
			'url_chapter': scraped_data['url chapter'],
			'url_metadata': scraped_data['url metadata'],
		}
		m = Manga(title=data_manga['title'], author=data_manga['author'], pub_status=data_manga['pub_status'], latest_chapter=data_manga['latest_chapter'], date_uploaded=date_uploaded, release_date=release_date, url_chapter=data_manga['url_chapter'], url_metadata=data_manga['url_metadata'])

		m.save()



class Manga(models.Model):

	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200, unique=True)
	author = models.CharField(max_length=200)
	pub_status = models.CharField(max_length=100)
	latest_chapter = models.IntegerField(default= 0)
	date_uploaded =  models.DateField(auto_now_add=True)
	release_date = models.DateField()

	url_chapter = models.CharField(max_length=200) # url_chapter can be the same url used for url_metadata
	url_metadata = models.CharField(max_length=200)

	objects = models.Manager()
	custom_objects = MangaManager()

	def __str__(self):
		return self.title

	def was_uploaded_recently(self):
		"""
		:return: Returns true if the manga was uploaded within the last 7 days
		"""
		now = timezone.now()
		return now - datetime.timedelta(days=7) <= self.date_uploaded <= now

# TODO: Complete MangaGenre model.
class MangaGenre(models.Model):
	manga = models.ForeignKey(Manga, on_delete = models.CASCADE)
	genre = models.CharField(max_length =200)

	class Meta:
		unique_together = (('manga', 'genre'),)

	def __str__(self):
		return (self.manga, self.genre)
	
# class MangaUser(models.Model):
# 	user = models.ForeignKey(User, on_delete= models.CASCADE)




