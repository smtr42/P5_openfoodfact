import os
import colorful as cf
from UI.print_out import input_yes_no, sentence
from apidata.requester import RequestData
from apidata.cleaner import Cleaner
from dbmanagement.manager.category_manager import CategoryManager
from dbmanagement.manager.product_manager import product_manager
from dbmanagement.manager.favorite_manager import FavoriteManager
from dbmanagement.manager.store_manager import StoreManager
from UI.fsm.main import device


def json_exists():
    """Test the existence of json files"""
    this_folder = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(this_folder, 'apidata/products_fr.json')
    print("data_file :", data_file)
    print("os path exists :", os.path.exists(data_file))
    if os.path.exists(data_file):
        print("It seems you have usable data")
    else:
        print(cf.red("IT SEEMS DATA IS MISSING - YOU MUST LET THE APPLICATION "
                     "DOWNLOAD DATA \n"))
    answer = input_yes_no(sentence["data"])
    if answer == 'y':
        rd = RequestData()
        rd.fetch_category()
        rd.fetch_products()
    else:
        pass


json_exists()

dataclean = Cleaner()
category_manager = CategoryManager()
favorite_manager = FavoriteManager()
store_manager = StoreManager()
data = dataclean.get_dict_data()

answer = input_yes_no(sentence["erase"])

if answer == 'y':
    product_manager.wipe_out()
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
