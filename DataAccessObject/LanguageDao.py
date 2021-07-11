from Model.Language import Language
from database import Database


class LanguageDao:
    database = None

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.database = database

    def create_table(self):
        self.database.execute_query(Language.create_sql, {})

    def initialize_data(self):
        # This is the qmark style:
        self.database.execute_query("insert into lang values (?, ?)", ("C", 1972))

        # The qmark style used with executemany():
        lang_list = [
            ("Fortran", 1957),
            ("Python", 1991),
            ("Go", 2009),
            ("Perl", 1984)
        ]
        self.database.execute_many_query("insert into lang values (?, ?)", lang_list)
        self.database.commit()

    def fetch_data(self, year):
        # And this is the named style:
        query = "select * from lang where first_appeared>=:year order by first_appeared"
        params = {"year": year}
        return self.database.fetch_all(query=query, parameters=params)
