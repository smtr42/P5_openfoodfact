from dbmanagement.database import db
from dbmanagement.models import Product
from apidata.cleaner import Cleaner

from dbmanagement.manager.category_manager import CategoryManager
from dbmanagement.manager.product_manager import ProductManager
from dbmanagement.manager.favorite_manager import FavoriteManager
from dbmanagement.manager.store_manager import StoreManager

import time


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





start_time = time.time()
print("starting main_manager")

dataclean = Cleaner()

category_manager = CategoryManager()
product_manager = ProductManager(Product)
favorite_manager = FavoriteManager()
store_manager = StoreManager()
main_manager = MainManager()

# print("Ditching old database")
# main_manager.drop_tables()
# print("Creating new databse and filling it")
# main_manager.create_tables()
# main_manager.populate_tables()



# 1 - Quel aliment souhaitez-vous remplacer ?
#     Sélectionnez la catégorie.
#         afficher 5 propositions
#         utilisateur séléectionne un chiffre et appuie sur entrée
#             Afficher 5 mauvais aliments de la catégorie précédemment sélectionnée
#             utilisateur sélectionne un chiffre et appuie sur entrée
#             afficher un substitut et son détail
#                 proposer la possiblité d'enregistrer l'aliment dans les favoris
#                 proposer de revenir au menu
# 2 - Retrouver mes aliments substitués.
#     affiche la liste des aliments substitués
#         l'utilisateur sélectionne un chiffre et appuie sur entrée' \
#             affichage de l'aliment sélectionné'


print("ran in {}s".format(time.time() - start_time))
