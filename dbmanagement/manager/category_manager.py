from dbmanagement.database import db


class CategoryManager:
    def create_category_table(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Category (
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          category_name VARCHAR(255) UNIQUE;
                      """)

    def insert_category(self, barcode, category, product_name, nutrigrade, url, store):
        for cat in category:
            db.query(""" INSERT INTO Category(cat) 
                            VALUES (:cat) ON DUPLICATE 
                            KEY UPDATE cat=:cat;
                        """, cat=cat)

    def populate_category_table(self):
        pass


category_manager = CategoryManager()
