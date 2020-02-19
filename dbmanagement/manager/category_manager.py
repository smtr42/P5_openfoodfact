from dbmanagement.database import db


class CategoryManager:

    def create_tables(self):
        db.query(""" CREATE TABLE IF NOT EXISTS Category (
                          id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          category_name VARCHAR(255) UNIQUE);
                      """)


