import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Manga
# Create your tests here.

class MangaModelTests(TestCase):

    def test_was_uploaded_recently_with_future_date(self):
        """
        :return: Returns False for manga whose date_uploaded is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_manga = Manga(date_uploaded=time)
        self.assertIs(future_manga.was_uploaded_recently(), False)

    def test_was_uploaded_recently_with_old_question(self):
        """
        :return: Returns False for manga whose date_uploaded is older than 7 days.
        """
        time = timezone.now() - datetime.timedelta(days=7, seconds=1)
        old_manga = Manga(date_uploaded=time)
        self.assertIs(old_manga.was_uploaded_recently(), False)