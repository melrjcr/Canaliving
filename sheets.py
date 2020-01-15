
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','canaliving.settings')

import django
django.setup()

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from website.models import Products




scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('/home/melcr/PycharmProjects/canaliving.com/canaliving/credscanaliving.json', scope)

client = gspread.authorize(creds)

sheet = client.open('CanaLiving_Product_List').sheet1  # Open the spreadhseet

r = sheet.get_all_records()  # Get a list of all records


def populate():

    for i in range(1,9):

        products_instance = Products(
            name = r[i]['Product'],
            category = r[i]['Category'],
            price = r[i]['Price'],
            short_description = r[i]['Short Description'],
            description = r[i]['Long Description'],
            size = r[i]['Size/Servin'],
            ingredients = r[i]['Ingredients'],
            image = r[i]['Image Location'],
             )
        products_instance.save()

populate()