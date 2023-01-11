import sqlite3
from data import ContentFile, ContentVersion

database_location = 'taxonomical-database.db'

CREATE_STRINGS = {
    'ContentFile' : "CREATE TABLE ContentFile(filename VARCHAR(255), filetype VARCHAR(255), fileextension: VARCHAR(25))",
    'ContentVersion': "CREATE TABLE ContentVersion(FOREIGN KEY(content_file) REFERENCES ContentFile(id), name VARCHAR(255), version VARCHAR(255), contents BLOB)"
}

class Database_impl:
    def __init__(self, location=database_location):
        self.location = location
        self.__create_tables__()

    def connection(self):
        return sqlite3.connect(self.location)

    def __database_tables__(self, cur):
        database_tables = []
        for database_table in cur.execute('SELECT name FROM sqlite_master').fetchall():
            database_tables.append(database_table[0])
        return database_tables

    def __create_tables__(self):
        self.tables = [ContentFile, ContentVersion]
        con = self.connection()
        cur = con.cursor()
        database_tables = self.__database_tables__(cur)
        for table in self.tables:
            if not database_tables.__contains__(table.__name__):
                cur.execute(CREATE_STRINGS.get(table.__name__))
        con.commit()
        con.close()

    def insert(self, content_files: list):
        con = self.connection()
        values = ''
        for record in content_files:
            values += f"{record.__value__()},"
        values = values.removesuffix(',')
        query = f"INSERT INTO {ContentFile.__name__} VALUES {values}"
        con.cursor().execute(query)
        con.commit()
        con.close()

DATABASE = Database_impl()