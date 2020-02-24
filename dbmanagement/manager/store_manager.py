from dbmanagement.database import db


class StoreManager:

    def create_tables(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Store (
                              id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                              store_name VARCHAR(255) UNIQUE);
                              """)
    @staticmethod
    def insert_into_store(store_name):
        db.query("""INSERT INTO Store(id, store_name)
                    VALUES(null, :store_name)
                    ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id), 
                    store_name=store_name;""",
                 store_name=store_name.strip(), )

    @staticmethod
    def insert_into_product_store(barcode, store_id):
        db.query("""INSERT INTO Product_store(product_barcode, store_id)
            values (:barcode, :store_id)
            ;
            """, barcode=barcode, store_id=store_id,)
