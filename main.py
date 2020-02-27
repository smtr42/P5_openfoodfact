"""This is the main file where everything come in together from download to
cleaning, insertion in database and FSM."""
import colorful as cf

from UI.fsm.main import device
from UI.print_out import input_yes_no, sentence
from apidata.cleaner import Cleaner
from apidata.requester import RequestData
from dbmanagement.manager.category_manager import CategoryManager
from dbmanagement.manager.favorite_manager import favorite_manager
from dbmanagement.manager.product_manager import product_manager
from dbmanagement.manager.store_manager import StoreManager

print(cf.red("IF IT IS THE FIRST TIME YOU USE THE APPLICATION, YOU MUST "
             "DOWNLOAD DATA AND RESET DATABASE \n"))
answer = input_yes_no(sentence["data"])
if answer == 'y':
    rd = RequestData()
    rd.fetch_category()
    rd.fetch_products()

dataclean = Cleaner()
category_manager = CategoryManager()
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

while True:
    device.show()
    event = device.input_checker()
    device.on_event(event)
