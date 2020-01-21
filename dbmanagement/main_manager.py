from dbmanagement.database import db
from dbmanagement.models import Product
from apidata.cleaner import Cleaner, dataclean

from dbmanagement.manager.category_manager import CategoryManager
from dbmanagement.manager.product_manager import ProductManager
from dbmanagement.manager.favorite_manager import FavoriteManager
from dbmanagement.manager.store_manager import StoreManager


class MainManager:
    def __init__(self, cleaner):
        self.cleaner = cleaner
        self.data = self.cleaner.get_dict_data()

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
        print(self.data)
        product_manager.insert_products(self.data)
        pass
        # data = self.data
        # for product in data:
        #     category_manager.insert_category(*product)
        #     # product_manager.insert_products(*product)
        #     # store_manager.insert_store(*product)


category_manager = CategoryManager()
product_manager = ProductManager(dataclean, Product)
favorite_manager = FavoriteManager()
store_manager = StoreManager()

main_manager = MainManager(Cleaner)
main_manager.drop_tables()
main_manager.create_tables()
main_manager.populate_tables()





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
