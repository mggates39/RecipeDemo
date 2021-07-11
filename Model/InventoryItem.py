
class InventoryItem:
    create_sql: str = """CREATE TABLE inventory_item (
        item_id   INTEGER NOT NULL PRIMARY KEY,
        name VARCHAR,
        description VARCHAR
        )"""

    def __init__(self, item_id, name, description) -> None:
        super().__init__()
        self.__item_id = item_id
        self.__name = name
        self.__description = description

    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, item_id):
        self.__item_id = item_id

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
