# -*- coding: utf-8 -*-
import requests
import json
from config import constant


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

        list_cat = constant.CATEGORIES
        resp = [x for x in self.list_cat if x in list_cat]

        self.list_cat = resp
        self.categories_to_json(resp)

    def fetch_products(self):
        """Request the products in respect for the categories loaded"""
        print("Requesting Products - Please wait")
        all_products = {}
        for category in self.list_cat:
            config = {"action": "process",
                      # Get the result by category
                      "tagtype_0": "categories",
                      # the tag represents the article search
                      'tag_0': category,
                      "tag_contains_0": "contains",
                      # Number of articles per page
                      # Min content 20, Max content 1000
                      "page_size": constant.PRODUCT_NUMBER,
                      # The API response in JSON
                      "json": 1}
            response = self.req(self.search_url, param=config)
            data = response.json()
            all_products[category] = data

        self.prod_to_json(all_products)
        print("products download and write success")

    def req(self, url, param=None):
        response = requests.get(url, param)
        return response

    def categories_to_json(self, obj):
        with open('apidata/localdata/categories_fr.json', 'w') as f:  # writing JSON object
            json.dump(obj, f)

    def prod_to_json(self, obj):
        with open('apidata/localdata/products_fr.json', 'w') as f:  # writing JSON object
            json.dump(obj, f)

    # def filter_category(self):
    #     """Filter category"""
    #     lister = []
    #
    #     for name in self.list_cat:
    #         if ':' not in name:
    #             temp = name.replace('-', ' ').replace('\'', ' ')
    #             lister.append(temp)
    #
    #     sampling = random.sample(lister, 20)
    #     self.list_cat = sampling


rd = RequestData()
rd.fetch_category()
rd.fetch_products()
