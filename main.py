import os
import colorful as cf
from apidata.requester import RequestData

from dbmanagement.database import db
# from dbmanagement.models import Product
from apidata.cleaner import Cleaner

from dbmanagement.manager.category_manager import CategoryManager
# from dbmanagement.manager.product_manager import ProductManager
from dbmanagement.manager.product_manager import product_manager
from dbmanagement.manager.favorite_manager import FavoriteManager
from dbmanagement.manager.store_manager import StoreManager
from UI.fsm.main import device

this_folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(this_folder, 'apidata/products_fr.json')
if not os.path.exists(data_file):
    print(cf.red("IT SEEMS DATA IS MISSING - YOU MUST LET THE APPLICATION "
                 "DOWNLOAD DATA \n"))


print(cf.white("Please " + cf.red('press "y" ', nested=True) + 'to do so'))
print(cf.white("Otherwise, " + cf.green('press any key ', nested=True) + 'to continue'))
answer = input(": ")

if answer == 'y':
    rd = RequestData()
    rd.fetch_category()
    rd.fetch_products()
else:
    pass

# import dbmanagement.manager.main
# main_manager = MainManager()
# main_manager.drop_tables()
dataclean = Cleaner()
category_manager = CategoryManager()
# product_manager = ProductManager(Product)
favorite_manager = FavoriteManager()
store_manager = StoreManager()
data = dataclean.get_dict_data()

answer = input(
    "Would you like to erase all the tables and fill them again ? "
    "Press 'y' if that's the case, otherwise press any key to use "
    "pre-existing database.")

if answer == 'y':
    print("Ditching old database...")
    db.query(""" DROP TABLE IF EXISTS
                      Product, Category, Store,
                      Favorite, Product_category,
                      Product_Store;
                    """)
    category_manager.create_tables()
    store_manager.create_tables()
    product_manager.create_tables()
    favorite_manager.create_tables()
    product_manager.insert_products(data)
else:
    pass

while True:
    device.show()
    event = device.input_checker()
    device.on_event(event)