from django.db import models

# Create your models here.
class Manga(models.Model):

	title = models.CharField(max_length=200, unique=True)
	author = models.CharField(max_length=200)
	pub_status = models.CharField(max_length=100)

# TODO: Complete MangaGenre model.
class MangaGenre(models.Model):



