from Model.Recipe import Recipe
from database import Database


class RecipeDao:
    database = None

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.database = database

    def create_table(self):
        self.database.execute_query(Recipe.create_sql, {})
