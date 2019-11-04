from dbmanagement.database import db


class ProductManager:

    def __init__(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Product (
                          barcode INT UNSIGNED UNIQUE PRIMARY KEY,
                          product_name VARCHAR(255) NOT NULL,
                          description VARCHAR(255),
                          nutriscore INT UNSIGNED
                          url VARCHAR(255));
                       """)

    def insert_product(self, barcode, category, product_name, nutrigrade, url,
                       store):
        for prod in category:
            db.query(""" INSERT INTO Product(prod) 
                            VALUES (:prod) ON DUPLICATE 
                            KEY UPDATE prod=:prod;
                        """, prod=prod)

    def populate_product_table(self):
        pass

    def search_healthier_than(self):
        pass


product_manager = ProductManager()
