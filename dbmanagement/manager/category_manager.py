from dbmanagement.database import db


class CategoryManager:
    """Class containing every method about the Category table"""

    def create_tables(self):
        """Create the Category table"""
        db.query(""" CREATE TABLE IF NOT EXISTS Category (
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          category_name VARCHAR(255) UNIQUE);
                      """)

    @staticmethod
    def get_cat():
        """Return the category name"""
        category_names = {}
        i = 1
        for row in db.query("""SELECT Category.category_name
                               FROM Category
                               ORDER BY RAND() LIMIT 5;"""):
            category_names[i] = row["category_name"]
            i += 1
        return category_names

    @staticmethod
    def insert_into_category(product):
        """Insert data into the Category table"""
        category = product["category"]
        db.query("""INSERT INTO Category(id, category_name)
                    VALUES(null, :category)
                    ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id),
                    category_name=:category;""",
                 category=category, )

    @staticmethod
    def insert_into_product_category(barcode, category_id):
        """Insert data into the association table"""
        db.query(
            """
            INSERT INTO Product_category(product_barcode, category_id)
            values (:barcode, :category_id)
            ;
            """,
            barcode=barcode, category_id=category_id, )
