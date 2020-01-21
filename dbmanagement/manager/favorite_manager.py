from dbmanagement.database import db


class FavoriteManager:

    def create_tables(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Favorite (
                          id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          product_barcode BIGINT UNSIGNED NOT NULL,
                          substitute_barcode BIGINT UNSIGNED NOT NULL,
                          
                          CONSTRAINT fk_favorite_substitute
                            FOREIGN KEY (substitute_barcode)
                            REFERENCES Product(barcode),
                          CONSTRAINT fk_favorite_product
                            FOREIGN KEY (product_barcode)
                            REFERENCES Product(barcode));
                        """)

    def save_prod_to_fav(self, product):
        """save in the db the selected substitute"""
        pass

    def get_all_favorite(self):
        """ retrieve all substitute saved by the user"""
        pass