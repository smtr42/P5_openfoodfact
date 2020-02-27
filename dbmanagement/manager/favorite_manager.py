from dbmanagement.database import db
from dbmanagement.manager.product_manager import product_manager

class FavoriteManager:
    """Contain methods about the Favorite Table"""

    def create_tables(self):
        """Create the Favorite Table"""
        db.query(""" CREATE TABLE IF NOT EXISTS Favorite (
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
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
        """Insert into the Favorite table a couple of barcode"""
        product_barcode = uh_barcode[event]
        substitute_barcode = sub_product["barcode"]

        db.query("""INSERT INTO Favorite(product_barcode, substitute_barcode)
        VALUES(:product_barcode, :substitute_barcode)
        ON DUPLICATE KEY UPDATE
        product_barcode=:product_barcode,
        substitute_barcode=:substitute_barcode;""",
                 product_barcode=product_barcode,
                 substitute_barcode=substitute_barcode)

    def get_all_favorite(self):
        """ retrieve all substitute saved by the user"""
        fav_name = {}
        fav_barcode = {}
        uh_barcode = {}
        i = 1
        for row in db.query("""SELECT Product.product_name, Product.barcode,
        Favorite.product_barcode, Favorite.substitute_barcode
                            FROM Product
                            INNER JOIN Favorite ON
                            Favorite.substitute_barcode=Product.barcode
                            """):
            uh_name = product_manager.get_product_by_barcode(
                row["product_barcode"])
            fav_name[i] = row["product_name"], row["substitute_barcode"], row[
                "product_barcode"], uh_name['product_name']
            fav_barcode[i] = row["barcode"], row["product_barcode"]
            i += 1

        return fav_name, fav_barcode


favorite_manager = FavoriteManager()
