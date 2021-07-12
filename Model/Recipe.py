
class Recipe:
    create_sql: str = """CREATE TABLE recipes (
        recipe_id   INTEGER NOT NULL PRIMARY KEY,
        name VARCHAR,
        description VARCHAR
    )"""

    def __init__(self, recipe_id, name, description) -> None:
        super().__init__()
        self.__recipe_id = recipe_id
        self.__name = name
        self.__description = description

    @property
    def recipe_id(self):
        return self.__recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        self.__recipe_id = recipe_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description
