import json
import os

from configuration import constant


class Cleaner:
    """ this class will handle the data formatting before db use"""

    def __init__(self):
        """ Initialize variables and launch filter_products"""
        self.keys = ['id', 'product_name_fr', 'nutrition_grade_fr',
                     'url', 'stores']
        self.list_cat = constant.CATEGORIES
        self._dict_data = []
        self.unicity = {"a": 1, }
        self.barcode_list = []
        self.filter_product()

    def filter_product(self):
        """  get the data from json files and run checks"""
        this_folder = os.path.dirname(os.path.abspath(__file__))
        try:
            my_file = os.path.join(this_folder, 'localdata/products_fr.json')
        except:
            print("You might have not downloaded the data...")
        with open(my_file, 'r') as json_file:
            data = json.load(json_file)
            for category in self.list_cat:
                products_s = data[category]['products']
                for element in products_s:
                    if self.data_exist(element):
                        self.data_format(element, category)

    def data_exist(self, element):
        """ run trough the data, if something's missing, it's discarded"""
        for x in self.keys:
            if x not in element or element[x] == "" or len(element["id"]) != 13:
                return False
        barcode = int(element['id'])
        if barcode not in set(self.barcode_list):
            self.barcode_list.append(barcode)
        else:
            return False
        return True

    def data_format(self, element, cat):
        """format the data so it's usable into a list of dictionary"""
        barcode = int(element['id'])
        category = cat
        product_name = element['product_name_fr']
        nutriscore = element['nutrition_grade_fr']
        url = element['url']

        store_list_lower = [x.lower() for x in element['stores'].split(",")]
        store = list(set(store_list_lower))

        dictionnaire = {"barcode": barcode, "category": category,
                        "product_name": product_name,
                        "nutriscore": nutriscore,
                        "url": url, "store": store, }
        self._dict_data.append(dictionnaire)

    def get_dict_data(self):
        """ retrieve the final data"""
        return self._dict_data
