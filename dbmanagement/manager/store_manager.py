from dbmanagement.database import db


class StoreManager:

    def create_tables(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Store (
                              id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                              store_name VARCHAR(255) UNIQUE);
                              """)

    # def insert_store(self, barcode, category, product_name, nutrigrade, url, store, *args, **kwargs):
    #     # split les différents stores possibles
    #     for stores in store:
    #         db.query(""" INSERT INTO Store(stores)
    #                         VALUES (:stores) ON DUPLICATE
    #                         KEY UPDATE stores=:stores;
    #                     """, stores=stores)
    #
    #         db.query(""" INSERT INTO Products_store
    #                         (product_barcode, store_id) VALUES (:product_barcode,
    #                         (SELECT id FROM Store WHERE store_name=:store));
    #                     """, product_barcode=barcode, store=store)
