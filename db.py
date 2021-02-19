from datetime import datetime
import psycopg2


host="ec2-3-214-3-162.compute-1.amazonaws.com"
port="ec2-3-214-3-162.compute-1.amazonaws.com"
database="d3jjpk34lg7877"
user="luxhnaoyygruuj"
password="9c00d5c200886fa961548a9356bac54d8f8565a6838e7a8d237754828c0a75dd"

def connect_db(query: str):
    """
    :param query:
    :return:
    """
    con = ""
    #con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    print("Database opened successfully")

    #TODO: correr esto una vez sola, una vez tengamos definido que poner en la db obviamente:
    """
    cur.execute('''CREATE TABLE STUDENT
          (ADMISSION INT PRIMARY KEY     NOT NULL,
          NAME           TEXT    NOT NULL,
          AGE            INT     NOT NULL,
          COURSE        CHAR(50),
          DEPARTMENT        CHAR(50));''')
    """

    return con

def save_db(db_con, query:str):
    cur = db_con.cursor()

    cur.execute(
        "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')");

    db_con.commit()
    print("Record inserted successfully")
    db_con.close()


def save_ticket(data: dict):
    #todo armar query
    return


def get_tickets_by_project(_id: int):
    content = [{
        'project_id': 1,
        'client_id': 1,
        'task_id': 1,
        'resource_id': 1,
        'id': 1,
        'status': 'en progreso soporte',
        'ticket_type': 'error',
        'description': 'bla bla bla',
        'priority': 3,
        'created_date': datetime(2020, 1, 1),
        'limit_date': datetime(2020, 1, 1)
    }]
    return content

def get_ticket_by_id(_id: int):
    #todo sacar este content y que sea una pegada trayendo de la db
    content = {
        'project_id': 1,
        'client_id': 1,
        'task_id': 1,
        'resource_id': 1,
        'id': 1,
        'status': 'en progreso soporte',
        'ticket_type': 'error',
        'description': 'bla bla bla',
        'priority': 3,
        'created_date': datetime(2020, 1, 1),
        'limit_date': datetime(2020, 1, 1)
    }
    return content

def get_projects():
    return