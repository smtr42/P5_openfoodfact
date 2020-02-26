"""This is a singleton, this will be imported where the use of the database
is needed"""
import records
from configuration import constant

db = records.Database(f"mysql+mysqlconnector://{constant.USER}:"
                      f"{constant.PASSWORD}@localhost/"
                      f"{constant.DATABASE_NAME}?charset=utf8mb4")
