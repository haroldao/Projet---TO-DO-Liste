# Import Sqlite3
import sqlite3 as sql
# Import de PrettyTable (affichage du tableau dans la console)
from prettytable import from_db_cursor


MENU_PROMPT = """
#=========================================
#Bienvenu sur l'interface NSI Todo Liste :
#=========================================
Quelle action souhaitez vous effectuez ? répondre par 1,2,3,4 ou 5:
1 - C - Créer une nouvelle tâche
2 - R - Consulter la liste des tâches + tâches (non terminée, terminée, urgentes)
3 - U - Modifier l'état d'une tâche.
4 - D - Supprimer une tâche.
5 - Quitter l'application

Je veux choisir l'option : """


def create_table():
    connection = sql.connect("todo.db")
    cursor = connection.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS todo(
            id INTEGER PRIMARY KEY,
            designation TEXT,
            echeance DATE,
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
    print("Liste complète de vos tâches ⏬\n", mytable)

    connection.close()


def delete_task(id):
    connection = sql.connect("todo.db")
    cursor = connection.cursor()

    query = '''
        DELETE
        FROM todo
        WHERE id = {}
    '''.format(id)

    cursor.execute(query)
    connection.commit()
    connection.close()


def show_task_status():
    connection = sql.connect("todo.db")
    cursor = connection.cursor()

    # Tache effectuée
    query_done = '''
        SELECT id, designation, echeance
        FROM todo
        WHERE etat="X"
    '''
    # Tache non effectuée
    query_not_done = '''
        SELECT id, designation, echeance
        FROM todo
        WHERE etat="O"
    '''

    query_emergency = '''
        SELECT * FROM todo
        WHERE echeance < date('now','+15 days')
        AND echeance > DATE("now")
    '''

    cursor.execute(query_done)
    mytable_done = from_db_cursor(cursor)
    print("\n\nTable des tâches terminées ⏬\n\n", mytable_done)

    cursor.execute(query_not_done)
    mytable_not_done = from_db_cursor(cursor)
    print("\n\nTable des tâches non terminées ⏬\n\n", mytable_not_done)

    cursor.execute(query_emergency)
    mytable_emergency = from_db_cursor(cursor)
    print("\n\nTable des tâches URGENTES ⏬\n\n", mytable_emergency)

    connection.commit()
    connection.close()


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
            which_table = input(
                '''Si vous souhaitez consulté votre liste de tâche, tapez 1.\nSi vous souhaitez consulté la liste des tachés non terminée, terminée, urgentes, tapez 2\n⏩ '''
            )

            if which_table == "1":
                show_table()
                see_another_table = input(
                    "Si vous souhaitez consulté la liste de vos tâches non terminée, terminée, urgentes, écrivez OUI sinon appuyer sur la touche ENTRER : ")
                if see_another_table == "Oui" or "OUI":
                    show_task_status()
                else:
                    input("🚧🚧 Pour revenir au menu, merci de presser ↩ ")

            elif which_table == "2":
                show_task_status()
                see_another_table = input(
                    "Si vous souhaitez consulté la liste complète de vos tâches, écrivez OUI sinon appuyer sur la touche ENTRER : ")
                if see_another_table == "Oui" or "OUI":
                    show_table()
                else:
                    input("🚧🚧 Pour revenir au menu, merci de presser ↩ ")
            else:
                pass

        elif user_input == "3":
            show_table()
            id = int(input("Entrer l'id: "))
            deadline = input("Entrer votre nouvelle échéance: ")
            update_deadline(id, deadline)
            input(
                "\n\nVos informations ont bien été mise à jour. Pressez la touche ↩ pour continuer ")
        elif user_input == "4":
            show_table()
            try:
                id = int(
                    input("Enter l'id de la tâche que vous souhaitez supprimer: "))
                delete_task(id)
            except ValueError:
                pass
            print("\nVotre tâche a bien été supprimée 😎")

        else:
            print("Oups... 😥... essayez encore !")


app()
