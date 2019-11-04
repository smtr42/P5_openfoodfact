from .database import db
from apidata.cleaner import Cleaner


class Product:
    def __init__(self, barcode, product_name, nutriscore, url, *args, **kwargs):
        self.barcode = barcode
        self.product_name = product_name
        self.nutriscore = nutriscore
        self.url = url


class Store:
    def __init__(self, store_name, *args, **kwargs):
        self.store_name = store_name


class Category:
    def __init__(self, category, *args, **kwargs):
        self.category = category


class Favorite:
    def __init__(self, product_barcode, substitute_barcode, *args, **kwargs):
        self.product_barcode = product_barcode
        self.substitute_barcode = substitute_barcode
