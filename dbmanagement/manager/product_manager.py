from dbmanagement.database import db
import time
from tqdm import tqdm


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
        """Elements insertion in database in tables product, Category, Product_category, Store, Product_store"""

        start_it_time = time.time()
        for product in tqdm(data, desc="Inserting products in database", total=len(data)):

            # insérer le produit en base
            # print("insertion dans Product")
            db.query("""INSERT INTO Product(barcode, product_name, nutriscore,
                                                                            url)
                        VALUES (:barcode, :product_name,:nutriscore, :url) 
                        ON DUPLICATE KEY UPDATE 
                            barcode=:barcode,product_name=:product_name,
                            nutriscore=:nutriscore, url=:url;
                        """, **product)

            # pour chaque store dans dans product on insert le store_name dans store:
            # print("insertion dans Store")
            for store_name in product["store"]:

                db.query("""INSERT INTO Store(id, store_name)
                            VALUES(null, :store_name)
                            ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id), 
                            store_name=store_name;""",
                         store_name=store_name.strip(), )

                store_id = None
                for row in db.query("""SELECT LAST_INSERT_ID() as id"""):
                    store_id = row["id"]
                barcode = product["barcode"]

                db.query(
                    """
                    INSERT INTO Product_store(product_barcode, store_id)
                    values (:barcode, :store_id)
                    ;
                    """,
                    barcode=barcode, store_id=store_id,
                )

            category = product["category"]
            db.query("""INSERT INTO Category(id, category_name)
                        VALUES(null, :category)
                        ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id), 
                        category_name=:category;""",
                     category=category, )

            category_id = None
            for row in db.query("""SELECT LAST_INSERT_ID() as id"""):
                category_id = row["id"]
            barcode = product["barcode"]

            db.query(
                """
                INSERT INTO Product_category(product_barcode, category_id)
                values (:barcode, :category_id)
                ;
                """,
                barcode=barcode, category_id=category_id,
            )
        print("all iteration ran in {}s".format(time.time() - start_it_time))
        print("fin")

    def get_unhealthy_prod_by_category(self, category):
        """ retrieve bad rated products by user's selected category"""
        input_category = category
        unhealthy_prod_by_cat = {}
        i = 1
        for row in db.query("""SELECT Product.product_name
                    FROM Product
                    INNER JOIN Product_category AS pc ON Product.barcode = pc.product_barcode
                    INNER JOIN Category  ON  pc.category_id = Category.id

                    WHERE Category.category_name = :input_category AND 
                    (Product.nutriscore = 'e' OR Product.nutriscore= 'd')
                    ORDER BY RAND() LIMIT 5
                    ;""", input_category=input_category):
            unhealthy_prod_by_cat[i] = row["product_name"]
            i += 1
        return unhealthy_prod_by_cat

    def get_healthier_product_by_category(self, category):
        """get a A or B rated randomized product to substitute to the unhealthy one selected"""
        input_category = category
        healthy_prod_by_cat, data = {}, {}
        i = 1
        for row in db.query("""SELECT Product.product_name, Product.barcode
                    FROM Product
                    INNER JOIN Product_category AS pc ON Product.barcode = pc.product_barcode
                    INNER JOIN Category  ON  pc.category_id = Category.id

                    WHERE Category.category_name = :input_category AND 
                    (Product.nutriscore = 'a' OR Product.nutriscore= 'b')
                    ORDER BY RAND() LIMIT 5
                    ;""", input_category=input_category):
            healthy_prod_by_cat[i] = row["product_name"]
            data[row["barcode"]] = row["product_name"]
            i += 1
        return healthy_prod_by_cat, data

    def save_healthy_product_to_favory(self):
        pass

    def get_product_by_name(self, name):
        input_name = name
        prod_by_name = {}
        for row in db.query("""SELECT Product.name, Product.nutriscore, Product.url, Product.barcode, Store.store_name
                    FROM Product
                    INNER JOIN Product_store AS ps ON ps.product_barcode=Product.barcode
                    INNER JOIN Store ON Store.id=ps.store_id
                    WHERE Product.product_name = :input_name;
                    """, input_name=input_name):
            print(row)
        return prod_by_name
        pass

#  !!!!! CRITICAL !!! modify writing in json file and store it in variable
# add this in trello
# modify retrieve product by name and replace by barcode
# transfert barcode to other states for better retrieval
# move function i product manager to better suited manager i.e store, category
# docstring
# pep8, flake8, black, docstring, import
# write down how to in the readme to use MySQL database and how to modify user and pwd
# modify trello board in accordance
# write the pdf 2 pages max
# prepare SQL graph and relations between tables
# Bonus : add multiple category by products for better accuracy when searching
#