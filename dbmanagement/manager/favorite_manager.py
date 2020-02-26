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

    def save_healthy_product_to_favorite(self, event, uh_barcode, sub_product):
        product_barcode = uh_barcode[event]
        substitute_barcode = sub_product["barcode"]

        db.query("""INSERT INTO Favorite(product_barcode, substitute_barcode)
        VALUES(:product_barcode, :substitute_barcode)
        ON DUPLICATE KEY UPDATE
        product_barcode=:product_barcode, substitute_barcode=:substitute_barcode
        ;""", product_barcode=product_barcode, substitute_barcode=substitute_barcode)

    def get_all_favorite(self):
        """ retrieve all substitute saved by the user"""
        fav_name = {}
        fav_barcode = {}
        i = 1
        for row in db.query("""SELECT Product.product_name, Product.barcode
                            FROM Product
                            INNER JOIN Favorite ON
                            Favorite.substitute_barcode=Product.barcode
                            """):
            fav_name[i] = row["product_name"]
            fav_barcode[i] = row["barcode"]
            i += 1
        return fav_name, fav_barcode  # return a tuple


favorite_manager = FavoriteManager()