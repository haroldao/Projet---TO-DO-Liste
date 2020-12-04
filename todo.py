# Import Sqlite3
import sqlite3 as sql
# Import de PrettyTable (affichage du tableau dans la console)
from prettytable import from_db_cursor


def app():
    user_selection = input(
        "1. C - Créer une nouvelle tâche\n2. R - Consulter la liste des tâches non-terminée, terminée, urgentes\n3. U - Modifier l'état d'une tâche\n4. D - Supprimer une tâche\n5. Quitter l'application")


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
