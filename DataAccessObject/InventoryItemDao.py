from Model.InventoryItem import InventoryItem
from database import Database


class InventoryItemDao:
    database = None

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.database = database

    def create_table(self):
        self.database.execute_query(InventoryItem.create_sql, {})
