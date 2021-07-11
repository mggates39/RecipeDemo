
class Language:
    create_sql: str = """create table lang (name, first_appeared)"""

    def __init__(self, name, first_appeared) -> None:
        super().__init__()
        self.__name = name
        self.__first_appeared = first_appeared

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def first_appeared(self):
        return self.__first_appeared

    @first_appeared.setter
    def first_appeared(self, first_appeared):
        self.__first_appeared = first_appeared

    def __str__(self) -> str:
        return "{} - {}".format(self.name, self.first_appeared)

