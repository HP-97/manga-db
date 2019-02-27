from django.urls import path
from django.conf.urls import url
from . import views
from manga.views import manga

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.manga, name='manga'),
]