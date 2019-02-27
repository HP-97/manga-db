from django.db import models
from django.contrib.auth.models import User
"""
References:

Foreign Key Django Model
https://stackoverflow.com/questions/14663523/foreign-key-django-model

Movie Database, storing multiple genres
https://stackoverflow.com/questions/17520720/movie-database-storing-multiple-genres/17520721
"""

# Create your models here.
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

	def __str__(self):
		return self.title

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




