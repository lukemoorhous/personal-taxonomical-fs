import sqlite3
from data import DTO,ContentFile, ContentVersion

database_location = 'taxonomical-database.db'

CREATE_STRING = {
    'ContentFile' : "CREATE TABLE ContentFile(id INTEGER primary key autoincrement, filename TEXT, filetype TEXT, fileextension TEXT)",
    'ContentVersion': "CREATE TABLE ContentVersion(id INTEGER primary key autoincrement, name TEXT, version TEXT, contents BLOB, content_file INTEGER, FOREIGN KEY(content_file) REFERENCES ContentFile(id))"
}

COLUMN_LIST = {
    'ContentFile' : ['id', 'filename', 'filetype', 'fileextension'],
    'ContentVersion' : ['id', 'name', 'version', 'content_file', 'contents']
}

class Database_impl:
    def __init__(self, location=database_location):
        self.location = location
        self.__create_tables__()

    def connection(self):
        return sqlite3.connect(self.location)

    def create(self, query):
        con = self.connection()
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        con.close()

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
                cur.execute(CREATE_STRING.get(table.__name__))
        con.commit()
        con.close()

    def insert_ContentFiles(self, records: list[ContentFile]):
        values = ''
        
        for record in records:
            values += f"{record.__repr__()},"
        values = values.removesuffix(',')
        query = f"INSERT INTO {ContentFile.__name__} ({COLUMN_LIST.get(ContentFile.__name__).__str__().strip('[,]')}) VALUES {values}"
        # print(query)
        self.create(query)

    def insert(self, records: list[DTO]):
        if records.__sizeof__() <= 0:
            return None
        cls = records[0].__class__
        cols = COLUMN_LIST.get(cls.__name__)
        records_vals = None
        for record in records:
            if record.__class__ != cls:
                raise TypeError('Cannot Insert multiple types in one operation')
            record_vals = None
            for col in cols:
                val = record.__getattribute__(col)
                if record_vals is None:
                    record_vals = f"'{val}'"
                else:
                    record_vals = f"{record_vals}, '{val}'"
            if records_vals is None:
                records_vals = f"({record_vals})"
            else:
                records_vals = f"{records_vals}, ({record_vals})"
        print(records_vals)

DATABASE = Database_impl()