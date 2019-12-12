# from dbmanagement.database import db
# from apidata.cleaner import Cleaner
# from dbmanagement.manager import category_manager, product_manager, favorite_manager, store_manager
#
#
# class MainManager:
#     def __init__(self, cleaner):
#         self.cleaner = cleaner
#         self.data = self.cleaner.get_data
#
#     def drop_tables(self):
#         db.query(""" DROP TABLE IF EXISTS
#                           Product, Category, Store,
#                           Favorite, Product_category,
#                           Product_Store;
#                         """)
#
#     def create_tables(self):
#         product_manager.create_product_table()
#         store_manager.create_store_table()
#         category_manager.create_category_table()
#         favorite_manager.create_table_favorite()
#         # create association tables
#
#
#     def populate_tables(self):
#         data = self.data
#         for product in data:
#             product_manager.insert_product(*product)
#             store_manager.insert_store(*product)
#             category_manager.insert_category(*product)
#         pass
#
#
# main_manager = MainManager(Cleaner)
#
# main_manager.drop_tables()
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