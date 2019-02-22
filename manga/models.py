from django.db import models

"""
References:

Foreign Key Django Model
https://stackoverflow.com/questions/14663523/foreign-key-django-model


"""

# Create your models here.
class Manga(models.Model):

	title = models.CharField(max_length=200, unique=True)
	author = models.CharField(max_length=200)
	pub_status = models.CharField(max_length=100)
	latest_chapter = models.IntegerField(default= 0)
	date_uploaded =  models.DateTimeField
	
	

# TODO: Complete MangaGenre model.
class MangaGenre(models.Model):
	manga = models.ForeignKey(Manga, on_delete = models.CASCADE)
	genre = models.CharField(max_length =200)
	
	class Meta:
		unique_together = (('manga', 'genre'),)
	
	



