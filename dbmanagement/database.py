import records
from config import constant


db = records.Database(f"mysql+mysqlconnector://{constant.USER}:{constant.PASSWORD}@localhost/"
                      f"{constant.DATABASE_NAME}?charset=utf8mb4")

