from dbmanagement.database import db


class CategoryManager:

    def insert_category(self, category):
        db.query(""" INSERT INTO Category(category_name) 
                        VALUES (:category) ON DUPLICATE
                        KEY UPDATE category_name=:category ;
                    """, category=category)

    # Insérer dans la table d'association Product_Category
    db.query("""INSERT INTO Product_category(id, product_barcode, category_id)
                VALUES(null, :barcode, :category_id) ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id), barcode=:barcode, ;
                """, barcode=product["barcode"], category_id=rows)

    def create_association_table_category(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Product_category ( 
                          id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          product_barcode INT ,
                          category_id INT )
                          CONSTRAINT product_category_category FOREIGN KEY (category_id) REFERENCES Category(id)
                          CONSTRAINT product_category_product FOREIGN KEY (product_barcode) REFERENCES Product(barcode)
                          );
                       """)

    def get_category(self):
        category = None
        for row in db.query("""SELECT * FROM Category as category"""):
            category = row["category"]
        return category

    def get_elements_from_category(self):
        db.query("""SELECT * FROM Product WHERE N
        """)



category_manager = CategoryManager()
