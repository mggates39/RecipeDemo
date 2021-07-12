from database import Database
from DataAccessObject.LanguageDao import LanguageDao
from DataAccessObject.RecipeDao import RecipeDao
from DataAccessObject.InventoryItemDao import InventoryItemDao
from DataAccessObject.IngredientDao import IngredientDao


class Repository:
    database = None
    language_dao = None
    recipe_dao = None
    inventory_item_dao = None
    ingredient_dao = None

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.database = database
        self.language_dao = LanguageDao(self.database)
        self.recipe_dao = RecipeDao(self.database)
        self.inventory_item_dao = InventoryItemDao(self.database)
        self.ingredient_dao = IngredientDao(self.database)

    def initialize_repository(self):
        self.database.connect()
        if not self.database.is_database_valid():
            self.language_dao.create_table()
            self.language_dao.initialize_data()
            self.recipe_dao.create_table()
            self.inventory_item_dao.create_table()
            self.inventory_item_dao.initialize_data()
            self.ingredient_dao.create_table()

        self.verify_database_version()

    def verify_database_version(self):
        database_version = self.database.get_actual_version()
        if database_version != self.database.get_expected_version():
            self.database.update_database(database_version)

    def get_language_data(self, year):
        return self.language_dao.fetch_data(year)

    def disconnect(self):
        self.database.disconnect()
