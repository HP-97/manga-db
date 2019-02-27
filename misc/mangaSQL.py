
from __future__ import print_function
from misc import mangaScrape
from datetime import date, datetime, timedelta
import mysql.connector

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
# with open(os.path.join(BASE_DIR, 'secret.json'), "r") as data_file:
# # 	data = json.load(data_file)
# #
# # config = {
# #     'user':
# # }