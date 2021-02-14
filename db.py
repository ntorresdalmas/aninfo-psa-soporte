from datetime import datetime


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