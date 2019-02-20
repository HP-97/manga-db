from django.db import models

# Create your models here.
class Manga(models.Model):
	title = models.CharField(max_length=200, unique=True)

	author = models.CharField()