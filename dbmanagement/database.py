import records

db = records.Database(f"mysql+mysqlconnector://{USER}:{PASSWORD}@localhost/"
                      f"{NAME}?charset=utf8mb4")
