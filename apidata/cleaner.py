import json
from config import constant


# ssi nutrigrade, nom, nutriscore présent
# nutrition-score-fr
# nutrition_grades

class Cleaner:
    def __init__(self):
        self.keys = ['id', 'product_name_fr', 'nutrition_grade_fr',
                     'url', 'stores']
        self.list_cat = constant.CATEGORIES
        self._result = []

    def filter_product(self):
        with open('localdata/products_fr.json') as json_file:
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
        return True

    def data_format(self, element, cat):
        barcode = element['id']
        category = cat
        product_name = element['product_name_fr']
        nutrigrade = element['nutrition_grade_fr']
        url = element['url']
        store = element['stores']

        product_tuple = (barcode, category, product_name, nutrigrade, url, store)
        self._result.append(product_tuple)

    @property
    def get_data(self):
        return self._result


cc = Cleaner()
cc.filter_product()
print(cc.get_data)
with open('localdata/data.json', 'w') as f:
    json.dump(cc.get_data, f)
