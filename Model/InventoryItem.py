
class InventoryItem:
    create_sql: str = """CREATE TABLE inventory_items (
        item_id   INTEGER NOT NULL PRIMARY KEY,
        parent_item_id INTEGER REFERENCES inventory_item,
        name VARCHAR,
        description VARCHAR
    )"""

    insert_query = """insert into inventory_items ( 
        name, 
        description,
        parent_item_id
    ) values (
        :name, 
        :description,
        :parent_item_id
    )"""

    def __init__(self, item_id, name, description, parent_item_id=None) -> None:
        super().__init__()
        self.__item_id = item_id
        self.__name = name
        self.__description = description
        self.__parent_item_id = parent_item_id

    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, item_id):
        self.__item_id = item_id

    @property
    def parent_item_id(self):
        return self.__parent_item_id

    @parent_item_id.setter
    def parent_item_id(self, parent_item_id):
        self.__parent_item_id = parent_item_id

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
