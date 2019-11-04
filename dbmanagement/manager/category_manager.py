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

    def create_association_table_category(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Product_category ( 
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          product_barcode INT ,
                          category_id INT )
                          CONSTRAINT product_category_category FOREIGN KEY (category_id) REFERENCES Category(id)
                          CONSTRAINT product_category_product FOREIGN KEY (product_barcode) REFERENCES Product(barcode)
                          );
                       """)

category_manager = CategoryManager()
