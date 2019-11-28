from dbmanagement.database import db


class CategoryManager:

    def insert_category(self, category):
        db.query(""" INSERT INTO Category(category_name) 
                        VALUES (:category) ON DUPLICATE
                        KEY UPDATE category_name=:category ;
                    """, category=category)


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
