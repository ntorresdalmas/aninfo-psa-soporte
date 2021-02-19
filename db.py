from datetime import datetime
import psycopg2 as psql
from contextlib import contextmanager

USER = "luxhnaoyygruuj"
HOST = "ec2-3-214-3-162.compute-1.amazonaws.com"
NAME = "d3jjpk34lg7877"
PORT = 5432
PASS = "9c00d5c200886fa961548a9356bac54d8f8565a6838e7a8d237754828c0a75dd"


@contextmanager
def cursor(name=None):
    with get_connection() as cn:
        try:
            yield cn.cursor(name=name) if name else cn.cursor()
            # psycopg connections do not autocommit.
            cn.commit()
        except:
            cn.rollback()


def get_connection():
    return psql.connect(user=USER, password=PASS, dbname=NAME, host=HOST, port=PORT)


def save_ticket(data: dict):
    query = '''insert into tickets (ticket_id, project_id, resource_id, task_id, name, status, type, 
                description,priority, creation_date, limit_date) VALUES (%(id)s, %(project_id)s, 
                %(resource_id)s, %(task_id)s, %(name)s, %(status)s, %(type)s, %(description)s, 
                %(priority)s, %(creation_date)s, %(limit_date)s)'''

    with cursor() as cur:
        cur.execute(query, data)


def get_tickets_by_project(_id: int):
    query = f'select * from tickets where project_id = {_id}'
    with cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
    return rows


def get_ticket_by_id(_id: int):
    query = f'select * from tickets where ticket_id = {_id}'
    with cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
    return rows[0]


def get_projects():
    query = """select * from projects"""
    with cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
    return rows


def edit_ticket(_id: str, data: dict):
    query = 'UPDATE TICKETS SET '
    query = query + " , ".join([f"{k} = %({k})s" for k, _ in data.items()])
    query = query + f" WHERE ticket_id = {_id}"
    with cursor() as cur:
        cur.execute(query, data)
