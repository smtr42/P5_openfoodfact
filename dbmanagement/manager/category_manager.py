from dbmanagement.database import db


class CategoryManager:

    def create_tables(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Category (
                          id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          category_name VARCHAR(255) UNIQUE);
                      """)

    def insert_category(self, data):
        pass

    def get_category(self):
        category = None
        for row in db.query("""SELECT * FROM Category as category"""):
            category = row["category"]
        return category

    def get_elements_from_category(self):
        db.query("""SELECT * FROM Product WHERE N
        """)

# category_manager = CategoryManager()
