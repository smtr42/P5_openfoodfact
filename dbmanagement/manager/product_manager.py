from dbmanagement.database import db


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

    def insert_products(self, data):
        # pour chaque produit dans data
        for product in data:
            # insérer le produit en base
            print("insertion dans Product")
            db.query("""INSERT INTO Product(barcode, product_name, nutriscore,
                                                                            url)
                        VALUES (:barcode, :product_name,:nutriscore, :url) 
                        ON DUPLICATE KEY UPDATE 
                            barcode=:barcode,product_name=:product_name,
                            nutriscore=:nutriscore, url=:url;
                        """, **product)

            # pour chaque store dans dans product on insert le store_name dans store:
            print("insertion dans Store")
            for store_name in product["store"]:
                db.query("""INSERT INTO Store(id, store_name)
                            VALUES(null, :store_name)
                            ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id), 
                            store_name=store_name;""",
                         store_name=store_name.strip().lower(), )

                store_id = None
                for row in db.query("""SELECT LAST_INSERT_ID() as id"""):
                    store_id = row["id"]
                barcode = product["barcode"]

                db.query(
                    """
                    INSERT INTO Product_store(product_barcode, store_id)
                    values (:barcode, :store_id)
                    ON DUPLICATE KEY UPDATE product_barcode=barcode;
                    """,
                    barcode=barcode, store_id=store_id,
                    # **product,
                )

            # # Insérer la catégorie dans Category
            # self.categorymanager.insert_category(product["category"])

        print("fin")

    def get_unhealthy_prod_by_category(self, category):
        """ retrieve 10 bad ratings products by user's selected category"""
        pass

    def get_healthier_product_by_category(self, category):
        """get a A or B rated randomized product to substitute to the unhealthy one selected"""
        pass

    def get_product_by_barcode(self, barcode):
        """ return the product full description after user selected a product"""
        pass



