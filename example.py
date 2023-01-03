import sqlite3

con = sqlite3.connect("tmp.db")
cur = con.cursor();

master_table = 'sqlite_master'
example_table = 'example'
example_columns = 'title, tag, date, content'


def get_table_row(table, name):
    query = f"SELECT name FROM {table} WHERE name='{name}'"
    return cur.execute(query)

def get_table(table, columns):
    query = f"SELECT {columns} FROM {table}"
    return cur.execute(query)

def create_table(table, columns):
    query = f"CREATE TABLE {table}({columns})"
    cur.execute(query)




def get_examples():
    if get_table_row(master_table, example_table).arraysize < 1:
        create_table(example_table, example_columns)
        cur.execute(f"""
            INSERT INTO {example_table} VALUES
                ('kek', 'meme; web;', julianday('December 21, 2022'), 'kekismus maximus'),
                ('cringe', 'meme; web;', julianday('August 29, 2022'), 'cringe bro')
        """)
        con.commit()

    res = get_table(example_table, example_columns)

    examples = []
    for example in res.fetchall():
        examples.append(example)
    
    con.close()

    return examples