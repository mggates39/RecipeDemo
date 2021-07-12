from Model.InventoryItem import InventoryItem
from database import Database


class InventoryItemDao:
    database = None

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.database = database

    def create_table(self):
        self.database.execute_query(InventoryItem.create_sql, {})

    def initialize_data(self):
        ingredient_list = [
            {"name": "egg", "description": "Whole Egg", "parent_item_id": None},
            {"name": "egg yolk", "description": "Yolk of Egg", "parent_item_id": 1},
            {"name": "egg white", "description": "White of Egg", "parent_item_id": 1},
            {"name": "white sugar", "description": "Refined White Sugar", "parent_item_id": None},
            {"name": "all-purpose flour", "description": "All Purpose Flour", "parent_item_id": None},
            {"name": "cornstarch", "description": "Cornstarch powder", "parent_item_id": None},
            {"name": "salt", "description": "Table Salt", "parent_item_id": None},
            {"name": "water", "description": "Tap Water", "parent_item_id": None},
            {"name": "lemon", "description": "Lemon Fruit", "parent_item_id": None},
            {"name": "sweet butter", "description": "Sweet Butter", "parent_item_id": None},
            {"name": "salted butter", "description": "Salted Butter", "parent_item_id": None},
            {"name": "pie crust", "description": "Prepared Pie Crust", "parent_item_id": None},
        ]
        self.database.execute_many_query(InventoryItem.insert_query, ingredient_list)
        self.database.commit()
