# -*- coding: utf-8 -*-
import requests
import json
import random


class RequestData:
    """ """

    def __init__(self):
        self.cat_url = "https://fr.openfoodfacts.org/categories.json"
        self.search_url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.list_cat = []
        self.list_prod = []

    def fetch_category(self):
        """Request the list of category from the API"""
        print("Requesting Categories - Please wait")
        try:
            response = self.req(self.cat_url)
            data = json.loads(response.text)
            self.list_cat = [i['name'] for i in data['tags']]
            print("Success ! Categories loaded")

        except requests.exceptions.Timeout as t:
            print("Request Timeout, please retry : ", t)
        except requests.exceptions.RequestException as err:
            print("Something went bad, please retry : :", err)

    def filter_category(self):
        """Filter category"""
        lister = []

        for name in self.list_cat:
            if ':' not in name:
                temp = name.replace('-', ' ').replace('\'', ' ')
                lister.append(temp)

        sampling = random.sample(lister, 20)
        self.list_cat = sampling

    def fetch_products(self):
        """Request the products in respect for the categories loaded"""
        print("Requesting Products - Please wait")
        print(self.list_cat)
        all_products = []
        for category in self.list_cat:
            config = {"action": "process",
                      # Get the result by category
                      "tagtype_0": "categories",
                      # the tag represents the article search
                      'tag_0': category,
                      "tag_contains_0": "contains",
                      # Number of articles per page
                      # Min content 20, Max content 1000
                      "page_size": 10,
                      # The API response in JSON
                      "json": 1}
            response = self.req(self.search_url, param=config)
            data = response.json()

            # self.list_prod = [i['name'] for i in data['products']]
            # print("Success ! Categories loaded")
            #
            # products_section = data['products']
            # for product in products_section:
            #     product['main_category'] = category
            # all_products.extend(products_section)

    def req(self, url, param=None):
        response = requests.get(url, param)
        return response

    def filter_products(self):
        pass


rd = RequestData()
rd.fetch_category()
# rd.filter_category()
rd.fetch_products()

# url = ("https://world.openfoodfacts.org/cgi/search.pl?"
#                 "action=process&tagtype_0=categories&tagtype_1=countries"
#                 "&tag_contains_1=france&page_size=1000&json=1")
# print(url)


# a= "https://world.openfoodfacts.org/cgi/search.pl?search_terms=banania&search_simple=1&action=process&json=1"
# response = requests.get(a)
# data = json.loads(response.text)
# print(data)
