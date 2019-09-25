from .database import db
from apidata.cleaner import Cleaner


class MainManager:

    def __init__(self, cleaner, prod_manager, store_manager, cat_manager):
        self.data = cleaner
        self.prod_manager = prod_manager
        self.store_manager = store_manager
        self.cat_manager = cat_manager

    def drop_tables(self):
        db.query(""" DROP TABLE IF EXISTS
                          Category, Product_category,
                          Product, Product_store,
                          Store, Favorite;
                      """)

    def create_tables(self):
        self.prod_manager.create_product_table()
        self.store_manager.create_store_table()
        self.cat_manager.create_category_table()
        # create association tables
        pass

    def populate_tables(self):
        data = self.data.get_data
        for product in data:
            self.prod_manager.insert_product(*product)
            self.store_manager.insert_store(*product)
            self.cat_manager.insert_category(*product)
        pass


class ProductManager:
    # def get_healthier_than(self):
    #     pass

    ###########CREATION PRODUCT ###########
    def create_product_table(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Product (
                          barcode INT UNSIGNED UNIQUE PRIMARY KEY,
                          product_name VARCHAR(255) NOT NULL,
                          description VARCHAR(255),
                          nutrigrade VARCHAR(255) ,
                          nutriscore INT UNSIGNED
                          url VARCHAR(255));
                       """)

    def insert_product(self, barcode, category, product_name, nutrigrade, url, store):
        for prod in category:
            db.query(""" INSERT INTO Product(prod) 
                            VALUES (:prod) ON DUPLICATE 
                            KEY UPDATE prod=:prod;
                        """, prod=prod)

    ###########OPERATION PRODUCT ###########
    def populate_product_table(self):
        pass

    def search_healthier_than(self):
        pass


class StoreManager:
    ###########CREATION STORE ###########
    def create_store_table(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Store (
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          store_name VARCHAR(255) UNIQUE);
                      """)

    def insert_store(self, barcode, category, product_name, nutrigrade, url, store):
        for stores in category:
            db.query(""" INSERT INTO Store(stores) 
                            VALUES (:stores) ON DUPLICATE 
                            KEY UPDATE stores=:stores;
                        """, stores=stores)

            db.query(""" INSERT INTO Products_stores
                            (product_id, store_id) VALUES (:barcode,
                            (SELECT id FROM Stores WHERE store=:store_id));
                        """, barcode=id, store_id=store)


    ###########OPERATION STORE ###########
    def save_store_table(self):
        pass


class CategoryManager:
    ###########CREATION CATEGORY ###########
    def create_category_table(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Category (
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          category_name VARCHAR(255) UNIQUE;
                      """)

    def insert_category(self, barcode, category, product_name, nutrigrade, url, store):
        for cat in category:
            db.query(""" INSERT INTO Category(cat) 
                            VALUES (:cat) ON DUPLICATE 
                            KEY UPDATE cat=:cat;
                        """, cat=cat)

    ###########OPERATION CATEGORY ###########
    def populate_category_table(self):
        pass


class FavoriteManager:
    ###########CREATION FAVORITE ###########

    def create_table_favorite(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Favory (
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
                          product_barcode INT NOT NULL,
                          substitute_barcode INT;                       
                      """)

    def create_association_table_favorite(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Product_category ( 
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          product_barcode INT REFERENCES Product(barcode),
                          category_name VARCHAR(255) REFERENCES Category(category_name));
                       """)

    ###########OPERATION FAVORITE ###########
    def save_into_favorite(self):
        pass

    def get_all_favorite(self):
        pass


main_manager = MainManager(Cleaner, ProductManager, StoreManager, CategoryManager)
