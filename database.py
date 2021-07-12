import sqlite3


class Database:
    version = '1'
    con = None
    cur = None
    
    def connect(self):
        if self.con is None:
            self.con = sqlite3.connect("example.db")
            self.con.row_factory = sqlite3.Row

    def is_database_valid(self) -> bool:
        self.create_cursor()
        try:
            self.fetch_all("select version from db_version", {})
            return True
        except sqlite3.DatabaseError:
            self.init_database_version()
            return False

    def get_expected_version(self):
        return self.version

    def get_actual_version(self):
        self.create_cursor()
        version = self.fetch_all("select version from db_version", {})
        return version[0][0]

    def update_database(self, new_database_version):
        self.cur.execute("update db_version ast version = :ver", {"ver": new_database_version})

    def create_cursor(self):
        self.connect()
        if self.cur is None:
            self.cur = self.con.cursor()

    def init_database_version(self):
        self.create_cursor()
        self.cur.execute("create table db_version ( version )")
        self.cur.execute("insert into db_version (version) values(:ver)", {"ver": self.version})

    def execute_query(self, query, parameters):
        self.create_cursor()
        self.cur.execute(query, parameters)

    def execute_many_query(self, query, parameters):
        self.create_cursor()
        self.cur.executemany(query, parameters)

    def commit(self):
        self.con.commit()

    def rollback(self):
        self.con.rollback()

    def fetch_all(self, query, parameters):
        self.create_cursor()
        self.cur.execute(query, parameters)
        return self.cur.fetchall()

    def close_cursor(self, commit=True):
        if self.cur is not None:
            if self.con.in_transaction:
                if commit:
                    self.con.commit()
                else:
                    self.con.rollback()
            self.cur.close()
            self.cur = None            

    def disconnect(self):
        if self.con is not None:
            self.close_cursor()
            self.con.close()
            self.con = None
