import json

import colorful as cf
import requests
from tqdm import tqdm

from configuration import constant


class RequestData:
    """ The class fetch the data and save it in to a json file"""

    def __init__(self):
        self.cat_url = "https://fr.openfoodfacts.org/categories.json"
        self.search_url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.list_cat = []
        self.list_prod = []

    def fetch_category(self):
        """Request the list of category from the API"""
        print("Initialization - Please wait")
        try:
            response = self.req(self.cat_url)
            data = json.loads(response.text)
            self.list_cat = [i['name'] for i in data['tags']]

        except requests.exceptions.Timeout as t:
            print(cf.red("Request Timeout, please retry : ", t))
        except requests.exceptions.RequestException as err:
            print(cf.red("Something went bad, please retry : :", err))

        list_cat = constant.CATEGORIES
        print("list_cat in requester :", list_cat)
        resp = [x for x in self.list_cat if x in list_cat]
        print("resp in requester :", resp)
        self.list_cat = resp
        self.categories_to_json(resp)

    def fetch_products(self):
        """Request the products in respect for the categories loaded"""
        print("API connexion and data transfer  - Please wait... \n"
              "It should takes less than a minute \n \n")
        all_products = {}
        for category in tqdm(self.list_cat, total=len(self.list_cat)):
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
        print(cf.green("\n Raw data is now downloaded successfully"))
        print("Now saving...")
        self.prod_to_json(all_products)
        print(cf.green("Success !"))

    def req(self, url, param=None):
        """ small request function used multiple times"""
        response = requests.get(url, param)
        return response

    def categories_to_json(self, obj):
        """saving categories to a json files"""
        with open('apidata/localdata/categories_fr.json', 'w') as f:
            json.dump(obj, f)

    def prod_to_json(self, obj):
        """save the products to a json file"""
        with open('apidata/localdata/products_fr.json', 'w') as f:
            json.dump(obj, f)
