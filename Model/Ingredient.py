
class Ingredient:
    create_sql: str = """CREATE TABLE ingredient (
        ingredient_id   INTEGER NOT NULL PRIMARY KEY,
        recipe_id       INTEGER REFERENCES recipe,
        item_id         INTEGER REFERENCES inventory_item,
        quantity_name VARCHAR,
        quantity REAL
        )"""

    def __init__(self, ingredient_id, recipe_id, item_id, quantity_name, quantity) -> None:
        super().__init__()
        self.__ingredient_id = ingredient_id
        self.__recipe_id = recipe_id
        self.__item_id = item_id
        self.__quantity_name = quantity_name
        self.__quantity = quantity

    @property
    def ingredient_id(self):
        return self.__ingredient_id

    @ingredient_id.setter
    def ingredient_id(self, ingredient_id):
        self.__ingredient_id = ingredient_id

    @property
    def recipe_id(self):
        return self.__recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        self.__recipe_id = recipe_id

    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, item_id):
        self.__item_id = item_id

    @property
    def quantity_name(self):
        return self.__quantity_name

    @quantity_name.setter
    def quantity_name(self, quantity_name):
        self.__quantity_name = quantity_name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
