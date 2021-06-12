import sqlite3

class Database:
    con = None
    cur = None
    
    def connect(self):
        if self.con is None:
            self.con = sqlite3.connect("examble.db")
    
    def create_cursor(self):
        self.connect()
        if self.cur is None:
            self.cur = self.con.cursor()
    
    def create_table(self):
        self.create_cursor()
        self.cur.execute("create table lang (name, first_appeared)")

        # This is the qmark style:
        self.cur.execute("insert into lang values (?, ?)", ("C", 1972))

        # The qmark style used with executemany():
        lang_list = [
            ("Fortran", 1957),
            ("Python", 1991),
            ("Go", 2009),
            ("Perl", 1984)
        ]
        self.cur.executemany("insert into lang values (?, ?)", lang_list)
        self.con.commit()

    def fetch_data(self, year):
        self.create_cursor()
        # And this is the named style:
        self.cur.execute("select * from lang where first_appeared>=:year order by first_appeared",
                         {"year": year})
        return(self.cur.fetchall())
    
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