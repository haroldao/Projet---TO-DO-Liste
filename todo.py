# Import Sqlite3
import sqlite3 as sql
# Import de PrettyTable (affichage du tableau dans la console)
from prettytable import from_db_cursor


MENU_PROMPT = """
#=========================================
#Bienvenu sur l'interface NSI Todo Liste :
#=========================================
Quelle action souhaitez vous effectuez ? répondre par 1,2,3,4 ou 5:
1 - C - Créer une nouvelle tache
2 - R - Consulter la liste des taches non terminée, terminée, urgentes
3 - U - Modifier l'état d'une tache.
4 - D - Supprimer une tache.
5 - Quitter l'application

Je veux choisir l'option : """


def app():

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            task_name = input("Entrer le nom de votre nouvelle tâche: ")
            date = input(
                "Entrer l'échéance (ex : 2020-12-10 (format : YYYY-MM-DD)): ")
            status = input(
                "Entrer le status (tâche termininée : X / tâche non-terminée : O): ")
            add_task(task_name, date, status)
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Oups... 😥... essayez encore !")


app()


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


def add_task(task_name, date, status):
    connection = sql.connect("todo.db")
    cursor = connection.cursor()

    query = '''
        INSERT INTO todo (designation, echeance, etat)
        VALUES (?, ?, ?)
    '''

    cursor.execute(query, (task_name, date, status))

    connection.commit()
    connection.close()
