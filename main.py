# -*- coding: utf-8 -*-
import requests
import json



class ReachApi:
    """ """
    def __init__(self):
        pass

    @staticmethod
    def fetch_category():
        raw_categories = requests.get("https://fr.openfoodfacts.org/categories.json")
        data = json.loads(raw_categories.text)
        list_dict_cat = data['tags']

        return list_dict_cat




tags = [{'name': 'jambon', 2.78: 'bbb', True: 'ccc'},{'name': 'saucisse', 2.78: 'bbb', False: 'ccc'},{'name': 'salade', 2.78: 'bbb', True: 'ccc'}]

for i in tags:
    name = i['name']
    # print(name)

a = [i['name'] for i in tags if i['name']=='jambon']
print("a= ", a)