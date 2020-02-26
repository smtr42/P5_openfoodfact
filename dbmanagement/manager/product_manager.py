import colorful as cf
from dbmanagement.database import db
from tqdm import tqdm
from dbmanagement.models import Product
from dbmanagement.manager.store_manager import StoreManager
from dbmanagement.manager.category_manager import CategoryManager


class ProductManager:

    def __init__(self, product):
        self.product = product

    def create_tables(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Product (
                          barcode BIGINT UNSIGNED UNIQUE PRIMARY KEY,
                          product_name VARCHAR(255) NOT NULL,
                          nutriscore CHAR(1),
                          url VARCHAR(255));
                        """)

        # creation des tables d'association
        db.query(""" CREATE TABLE IF NOT EXISTS Product_category (
                            id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                            product_barcode BIGINT UNSIGNED,
                            category_id BIGINT UNSIGNED,

                            CONSTRAINT fk_productbarcode_barcode 
                                FOREIGN KEY (product_barcode)
                                REFERENCES Product(barcode),
                            CONSTRAINT fk_categoryid_id
                                FOREIGN KEY (category_id)
                                REFERENCES Category(id));
                            """)
        db.query(""" CREATE TABLE IF NOT EXISTS Product_store(
                            id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                            product_barcode BIGINT UNSIGNED,
                            store_id BIGINT UNSIGNED,
                            UNIQUE(product_barcode, store_id),
                            
                            CONSTRAINT fk_productbarcodestore_barcode
                                FOREIGN KEY (product_barcode)
                                REFERENCES Product(barcode),
                            CONSTRAINT fk_storeid_id
                                FOREIGN KEY (store_id)
                                REFERENCES Store(id));
                            """)

    def insert_products(self, data):
        """Elements insertion in database in tables product, Category,
        Product_category, Store, Product_store"""

        for product in tqdm(
                data, desc="Inserting products in database", total=len(data)):

            db.query("""INSERT INTO Product(barcode, product_name, nutriscore,
                                                                            url)
                        VALUES (:barcode, :product_name,:nutriscore, :url) 
                        ON DUPLICATE KEY UPDATE 
                            barcode=:barcode,product_name=:product_name,
                            nutriscore=:nutriscore, url=:url;
                        """, **product)

            for store_name in product["store"]:
                StoreManager.insert_into_store(store_name)
                barcode, store_id = self.last_insert_id(product)
                StoreManager.insert_into_product_store(barcode, store_id)

            CategoryManager.insert_into_category(product)
            barcode, category_id = self.last_insert_id(product)
            CategoryManager.insert_into_product_category(barcode, category_id)

    def last_insert_id(self, product):
        id = None
        for row in db.query("""SELECT LAST_INSERT_ID() as id"""):
            id = row["id"]
        barcode = product["barcode"]
        return barcode, id

    def get_unhealthy_prod_by_category(self, category):
        """ retrieve bad rated products by user's selected category"""
        input_category = category
        unhealthy_prod_by_cat = {}
        # i = 1
        for row in db.query("""SELECT Product.product_name, Product.barcode
                    FROM Product
                    INNER JOIN Product_category AS pc 
                    ON Product.barcode = pc.product_barcode
                    INNER JOIN Category  ON  pc.category_id = Category.id
                    WHERE Category.category_name = :input_category AND 
                    (Product.nutriscore = 'e' OR Product.nutriscore= 'd')
                    ORDER BY RAND() LIMIT 5
                    ;""", input_category=input_category):
            unhealthy_prod_by_cat[row["barcode"]] = row["product_name"]

            # unhealthy_prod_by_cat[i] = row["product_name"]
            # i += 1
        return unhealthy_prod_by_cat

    def get_healthier_product_by_category(self, category):
        """get a A or B rated randomized product to substitute to the unhealthy
        one selected"""
        input_category = category
        healthy_prod_by_cat, data = {}, {}

        for row in db.query("""SELECT Product.product_name, Product.barcode
                    FROM Product
                    INNER JOIN Product_category AS pc 
                    ON Product.barcode = pc.product_barcode
                    INNER JOIN Category  ON  pc.category_id = Category.id

                    WHERE Category.category_name = :input_category AND 
                    (Product.nutriscore = 'a' OR Product.nutriscore= 'b')
                    ORDER BY RAND() LIMIT 5
                    ;""", input_category=input_category):
            healthy_prod_by_cat[row["barcode"]] = row["product_name"]
        return healthy_prod_by_cat

    def wipe_out(self):
        print("Ditching old database...")
        db.query(""" DROP TABLE IF EXISTS
                          Product, Category, Store,
                          Favorite, Product_category,
                          Product_Store;
                        """)
        print(cf.green("Database is now clean !"))

    def get_product_by_barcode(self, barcode):
        pbarcode = barcode
        prod_by_barcode = {}
        store_list = []
        for row in db.query("""SELECT Product.product_name, Product.nutriscore,
         Product.url, Product.barcode, Store.store_name
                    FROM Product
                    INNER JOIN Product_store AS ps 
                    ON ps.product_barcode=Product.barcode
                    INNER JOIN Store ON Store.id=ps.store_id
                    WHERE Product.barcode = :pbarcode;
                    """, pbarcode=pbarcode):
            store_list.append(row["store_name"])
            prod_by_barcode.update(row)
        prod_by_barcode["store_name"] = store_list

        return prod_by_barcode


product_manager = ProductManager(Product)
