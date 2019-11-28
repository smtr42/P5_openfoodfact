from dbmanagement.database import db
from apidata.cleaner import dataclean
from dbmanagement.models import Product
from dbmanagement.manager.category_manager import category_manager


class ProductManager:

    def __init__(self, cleaner, product, categorymanager):
        self.data = cleaner.get_dict_data
        self.product = product
        self.categorymanager = categorymanager

        db.query(""" DROP TABLE IF EXISTS
                          Product, Category, Store,
                          Favorite, Product_category,
                          Product_Store;
                        """)

        db.query(""" CREATE TABLE IF NOT EXISTS Product (
                          barcode BIGINT UNSIGNED UNIQUE PRIMARY KEY,
                          product_name VARCHAR(255) NOT NULL,
                          nutriscore CHAR(1),
                          url VARCHAR(255));
                        """)
        db.query(""" CREATE TABLE IF NOT EXISTS Category (
                          id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          category_name VARCHAR(255) UNIQUE);
                      """)
        # db.query(""" CREATE TABLE IF NOT EXISTS Favorite (
        #                   id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        #                   product_barcode INT NOT NULL,
        #                   substitute_barcode INT
        #                   CONSTRAINT fk_favorite_substitute
        #                     FOREIGN KEY (substitute_barcode)
        #                     REFERENCES Product(barcode)
        #                   CONSTRAINT fk_favorite_product
        #                     FOREIGN KEY (product_barcode)
        #                     REFERENCES Product(barcode)
        #                   );
        #                 """)
        db.query(""" CREATE TABLE IF NOT EXISTS Store (
                          id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          store_name VARCHAR(255) UNIQUE);
                          """)
        # creation des tables d'association
        db.query(""" CREATE TABLE IF NOT EXISTS Product_category (
                            id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                            product_barcode BIGINT UNSIGNED UNIQUE,
                            category_id INT NOT NULL,
                            
                            CONSTRAINT fk_productbarcode_barcode 
                                FOREIGN KEY (product_barcode)
                                REFERENCES Product(barcode),
                            CONSTRAINT fk_categoryid_id
                                FOREIGN KEY (product_barcode)
                                REFERENCES Category(id));
                            """)
        db.query(""" CREATE TABLE IF NOT EXISTS Product_store(
                            id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                            product_barcode BIGINT UNSIGNED UNIQUE,
                            store_id BIGINT UNSIGNED UNIQUE,
                            
                            CONSTRAINT fk_productbarcodestore_barcode
                                FOREIGN KEY (product_barcode)
                                REFERENCES Product(barcode),
                            CONSTRAINT fk_storeid_id
                                FOREIGN KEY (store_id)
                                REFERENCES Store(id));
                            """)
        self.insert_products(self.data)

    def insert_products(self, data):
        # pour chaque produit dans data
        for product in data:
            # insérer le produit en base
            db.query("""INSERT INTO Product(barcode, product_name, nutriscore,
                                                                            url)
                        VALUES (:barcode, :product_name,:nutriscore, :url) 
                        ON DUPLICATE KEY UPDATE 
                            barcode=:barcode,product_name=:product_name,
                            nutriscore=:nutriscore, url=:url;
                        """, **product)
            # Insérer la catégorie dans Category
            self.categorymanager.insert_category(product["category"])

            # Insérer dans la table d'association Product_Category
            rows = db.query(
                """ SELECT LAST_INSERT_ID()""")
            db.query("""INSERT INTO Product_category(product_barcode, category_id)
                        VALUES(:barcode, :category_id)
                        ;
                        """, barcode=product["barcode"], category_id=rows)

            # pour chaque magasin dans dans product:
            for stores in product["stores"]:
                db.query("""INSERT INTO Store(store_name)
                            VALUES(:stores) ON DUPLICATE KEY UPDATE 
                            store_name=:stores;""", stores=stores)
        print("fin")

    def get_product_by_barcode(self, barcode):
        pass


print("product manager is running")
product_manager = ProductManager(dataclean, Product, category_manager)
