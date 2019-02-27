
import django_tables2 as tables
from .models import Manga

class MangaTable(tables.Table):
    class Meta:
        model = Manga
        template_name = 'django_tables2/bootstrap.html'