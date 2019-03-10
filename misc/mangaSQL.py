
from __future__ import print_function
from common.util import mangaScrape
from datetime import date, datetime, timedelta
import mysql.connector

import os
import json

"""
References:

4/03/2019 - Connecting to MySQL using Connector/Python
https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

5/03/2019 - Inserting Data Using Connector/Python
https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Get details of MySQL database from secret.json
with open(os.path.join(BASE_DIR, 'secret.json'), "r") as data_file:
	data = json.load(data_file)

config = {
    'user': data["mysql_details"]["username"],
    'password': data["mysql_details"]["password"],
    'host': 'localhost',
    'port': '3306',
}

data_file.close()

cnx = mysql.connector.connect(user = config['user'], password= config['password'], host = config['host'], port = config['port'], database = 'manga_db')
cursor = cnx.cursor()

add_manga = ("INSERT INTO manga_manga "
               "(title, author, pub_status, latest_chapter, date_uploaded, release_date, url_chapter, url_metadata) "
               "VALUES (%(title)s, %(author)s, %(pub_status)s, %(latest_chapter)s, %(date_uploaded)s, %(release_date)s, %(url_chapter)s, %(url_metadata)s)")

add_mangagenre = ("INSERT INTO manga_mangagenre "
               "(manga_id, genre) "
               "VALUES (%(title)s, %(author)s, %(pub_status)s, %(latest_chapter)s, %(date_uploaded)s, %(release_date)s, %(url_chapter)s, %(url_metadata)s)")

# Insert manga information
scraped_data = mangaScrape.retrieve_data("https://jaiminisbox.com/reader/series/we-can-t-study", "https://myanimelist.net/manga/103890/Bokutachi_wa_Benkyou_ga_Dekinai")

date_uploaded = datetime.strptime(scraped_data['date uploaded'], '%d/%m/%Y')
release_date =  datetime.strptime(scraped_data['release date'], '%b %d, %Y')

# print(scraped_data['date uploaded'], scraped_data['release date'])
# print(date_uploaded, release_date)


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
try:
    cursor.execute(add_manga, data_manga)
except mysql.connector.Error as err:
    print("Something went wrong: {%s}" % err)



# Make sure the data is committed to the database
cnx.commit()

cursor.close()
cnx.close()