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


def add_task(task_name, deadline, status):
    connection = sql.connect("todo.db")
    cursor = connection.cursor()

    query = '''
        INSERT INTO todo (designation, echeance, etat)
        VALUES (?, ?, ?)
    '''

    cursor.execute(query, (task_name, deadline, status))

    connection.commit()
    connection.close()


def update_deadline(id, deadline):
    connection = sql.connect("todo.db")
    cursor = connection.cursor()

    if deadline != "":
        query = '''
        UPDATE todo
        SET echeance = '{}'
        WHERE id = {}'''.format(deadline, id)

    else:
        print(
            "La tâche que vous souhaitez n'exite pas ou vérifiez que l'échéance est bonne")

    cursor.execute(query)
    all_rows = cursor.fetchall()
    connection.commit()
    connection.close()


def show_table():
    connection = sql.connect("todo.db")
    cursor = connection.cursor()

    query = '''
        SELECT * 
        FROM TODO
    '''

    cursor.execute(query)
    connection.commit()

    mytable = from_db_cursor(cursor)
    print("La table actuellement ⏬\n", mytable)

    connection.close()


def delete_task(id):


create_table()


######################## Application #######################

def add_data(task_name, deadline, status):
    add_task(task_name, deadline, status)


def app():

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            task_name = input("Entrer le nom de votre nouvelle tâche: ")
            deadline = input(
                "Entrer l'échéance (ex : 2020-12-10 (format : YYYY-MM-DD)): ")
            status = input(
                "Entrer le status (tâche termininée : X / tâche non-terminée : O): ")
            add_data(task_name, deadline, status)
        elif user_input == "2":
            pass
        elif user_input == "3":
            id = int(input("Entrer l'id: "))
            show_table()
            deadline = input("Entrer votre nouvelle échéance: ")
            update_deadline(id, deadline)
            input("\n\nVos informations ont bien été mise à jour.")
        elif user_input == "4":
            pass
        else:
            print("Oups... 😥... essayez encore !")


app()
