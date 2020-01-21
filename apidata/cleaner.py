import json
import os
from configuration import constant


class Cleaner:
    def __init__(self):
        self.keys = ['id', 'product_name_fr', 'nutrition_grade_fr',
                     'url', 'stores']
        self.list_cat = constant.CATEGORIES
        self._result = []
        self._dict_data = []
        self.filter_product()

    def filter_product(self):
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'localdata/products_fr.json')
        with open(my_file) as json_file:
            data = json.load(json_file)
            for category in self.list_cat:
                products_s = data[category]['products']
                for element in products_s:
                    if self.data_exist(element):
                        self.data_format(element, category)

    def data_exist(self, element):
        for x in self.keys:
            if x not in element or element[x] == "":
                return False
        if len(element["id"]) != 13 or element["id"] in self._dict_data:
            return False
        return True

    def data_format(self, element, cat):
        barcode = int(element['id'])
        category = cat
        product_name = element['product_name_fr']
        nutriscore = element['nutrition_grade_fr']
        url = element['url']
        store = element['stores'].split(",")

        dictionnaire = {"barcode": barcode, "category": category,
                        "product_name": product_name, "nutriscore": nutriscore,
                        "url": url, "store": store, }
        self._dict_data.append(dictionnaire)

        product_tuple = (
            barcode, category, product_name, nutriscore, url, store,)
        self._result.append(product_tuple)

    @property
    def get_data(self):
        return self._result

    def get_dict_data(self):
        return self._dict_data
