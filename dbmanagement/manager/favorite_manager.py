from dbmanagement.database import db


class FavoriteManager:

    def create_table_favorite(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Favorite (
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
                          product_barcode INT NOT NULL,
                          substitute_barcode INT;                       
                      """)

    def create_association_table_favorite(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Product_category ( 
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          product_barcode INT REFERENCES Product(barcode),
                          category_name VARCHAR(255) REFERENCES Category(category_name));
                       """)

    def save_into_favorite(self):
        pass

    def get_all_favorite(self):
        pass


favorite_manager = FavoriteManager()
