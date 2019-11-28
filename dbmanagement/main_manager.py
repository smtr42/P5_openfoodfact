# from dbmanagement.database import db
# from apidata.cleaner import Cleaner
# from dbmanagement.manager import category_manager, product_manager, favorite_manager, store_manager
#
#
# class MainManager:
#     def __init__(self, cleaner):
#         self.cleaner = cleaner
#         self.data = self.cleaner.get_data
#     def drop_tables(self):
#         db.query(""" DROP TABLE IF EXISTS
#                           Category, Product_category,
#                           Product, Product_store,
#                           Store, Favorite;
#                       """)
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
