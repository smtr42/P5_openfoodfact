from dbmanagement.database import db


class StoreManager:

    def create_tables(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Store (
                              id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                              store_name VARCHAR(255) UNIQUE);
                              """)

    def insert_into_store(self, store_name):
        pass

    def insert_into_product_store(self, barcode, store_id):
        pass
