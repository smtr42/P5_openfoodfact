from dbmanagement.database import db


class StoreManager:
    """The StoreManager class has all methods about Store table"""

    def create_tables(self):
        """Create the Store table"""
        db.query(""" CREATE TABLE IF NOT EXISTS Store (
                              id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                              store_name VARCHAR(255) UNIQUE);
                              """)

    @staticmethod
    def insert_into_store(store_name):
        """Insert the data into the Store table"""
        db.query("""INSERT INTO Store(id, store_name)
                    VALUES(null, :store_name)
                    ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id),
                    store_name=store_name;""",
                 store_name=store_name.strip(), )

    @staticmethod
    def insert_into_product_store(barcode, store_id):
        """Insert data into the association table"""
        db.query("""INSERT INTO Product_store(product_barcode, store_id)
            values (:barcode, :store_id)
            ;
            """, barcode=barcode, store_id=store_id, )
