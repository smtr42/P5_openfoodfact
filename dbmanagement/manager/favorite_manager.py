from dbmanagement.database import db


class FavoriteManager:

    def create_table_favorite(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Favorite (
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
                          product_barcode INT NOT NULL,
                          substitute_barcode INT
                          CONSTRAINT favorite_substitute FOREIGN KEY (substitute_barcode) REFERENCES Product(barcode)
                          CONSTRAINT favorite_product FOREIGN KEY (product_barcode) REFERENCES Product(barcode)
                          );
                       """)



    def save_into_favorite(self):
        pass

    def get_all_favorite(self):
        pass


favorite_manager = FavoriteManager()
