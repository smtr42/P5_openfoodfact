from dbmanagement.database import db
from dbmanagement.models import Product
from apidata.cleaner import Cleaner

from dbmanagement.manager.category_manager import CategoryManager
from dbmanagement.manager.product_manager import ProductManager
from dbmanagement.manager.favorite_manager import FavoriteManager
from dbmanagement.manager.store_manager import StoreManager


class MainManager:
    def __init__(self):
        self.data = dataclean.get_dict_data()

    def drop_tables(self):
        db.query(""" DROP TABLE IF EXISTS
                          Product, Category, Store,
                          Favorite, Product_category,
                          Product_Store;
                        """)

    def create_tables(self):
        category_manager.create_tables()
        store_manager.create_tables()
        product_manager.create_tables()
        favorite_manager.create_tables()

    def populate_tables(self):
        product_manager.insert_products(self.data)


def run():

    dataclean = Cleaner()

    category_manager = CategoryManager()
    product_manager = ProductManager(Product)
    favorite_manager = FavoriteManager()
    store_manager = StoreManager()
    main_manager = MainManager()

    answer = input(
        "Would you like to erase all the tables and fill them again ? Press 'y' if "
        "that's the case, press any key to use pre-existing database.")
    if answer == 'y':
        print("Ditching old database")
        main_manager.drop_tables()
        print("Creating new tables and filling it")
        main_manager.create_tables()
        main_manager.populate_tables()
    else:
        pass
