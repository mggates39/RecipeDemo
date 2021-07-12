from Model.Ingredient import Ingredient
from database import Database


class IngredientDao:
    database = None

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.database = database

    def create_table(self):
        self.database.execute_query(Ingredient.create_sql, {})
