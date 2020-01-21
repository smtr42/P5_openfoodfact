from dbmanagement.database import db


class ProductManager:

    def __init__(self, cleaner, product):
        self.data = cleaner.get_dict_data
        self.product = product
        # self.insert_products(self.data)

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
            db.query("""INSERT INTO Product(barcode, product_name, nutriscore,
                                                                            url)
                        VALUES (:barcode, :product_name,:nutriscore, :url) 
                        ON DUPLICATE KEY UPDATE 
                            barcode=:barcode,product_name=:product_name,
                            nutriscore=:nutriscore, url=:url;
                        """, **product)

            # pour chaque store dans dans product on insert le store_name dans store:
            for store_name in product["stores"].split(","):
                db.query("""INSERT INTO Store(id, name)
                            VALUES(null, :name) ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id), 
                            name=:store_name;""",
                         store_name=store_name.strip().lower())  # id de Store ? simple ou "last insert id" ?

                store_id = None
                for row in db.query("""SELECT LAST_INSERT_ID() as id"""):
                    store_id = row["id"]
                barcode = product["barcode"]

                db.query(
                    """
                    INSERT INTO Product_store(product_barcode, store_id)
                    values (:barcode, store_id);
                    """,
                    barcode=barcode, store_id=store_id,
                    **product,
                )

            # # Insérer la catégorie dans Category
            # self.categorymanager.insert_category(product["category"])

        print("fin")

    def get_product_by_barcode(self, barcode):
        pass


print("product manager is running")
# product_manager = ProductManager(dataclean, Product, category_manager)
