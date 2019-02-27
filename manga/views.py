from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponse
from .tables import MangaTable
from .models import Manga

# Create your views here.

# def index(request):
# 	return HttpResponse("deez nutz.")

def manga(request):
	table = MangaTable(Manga.objects.all())
	RequestConfig(request).configure(table)
	return render(request, 'manga/index.html', {'manga': table})
