from dbmanagement.database import db


class StoreManager:
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

            db.query(""" INSERT INTO Products_store
                            (product_barcode, store_id) VALUES (:product_barcode,
                            (SELECT id FROM Store WHERE store_name=:store));
                        """, product_barcode=barcode, store=store)

    def save_store_table(self):
        pass


store_manager = StoreManager()
