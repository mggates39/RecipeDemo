from database import Database
from DataAccessObject.LanguageDao import LanguageDao


class Repository:
    database = None
    lang_dao = None

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.database = database
        self.lang_dao = LanguageDao(self.database)

    def initialize_repository(self):
        self.database.connect()
        if not self.database.is_database_valid():
            self.lang_dao.create_table()
            self.lang_dao.initialize_data()

        self.verify_database_version()

    def verify_database_version(self):
        database_version = self.database.get_actual_version()
        if database_version != self.database.get_expected_version():
            self.database.update_database(database_version)

    def get_language_data(self, year):
        return self.lang_dao.fetch_data(year)

    def disconnect(self):
        self.database.disconnect()
