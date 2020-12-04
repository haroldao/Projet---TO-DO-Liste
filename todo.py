# Import Sqlite3
import sqlite3 as sql
# Import de PrettyTable (affichage du tableau dans la console)
from prettytable import from_db_cursor


def create_table():
    connection = sql.connect("todo.db")
    cursor = connection.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS todo(
            id INTEGER PRIMARY KEY,
            designation TEXT,
            echeance TEXT,
            etat TEXT
        )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()
