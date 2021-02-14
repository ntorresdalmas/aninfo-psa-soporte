from datetime import datetime
from ticket import Ticket
from project import Project
import db


def create_ticket(content):
    #todo borrar este content cuando ya se reciba por parametro
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
    ticket = Ticket(**content)
    db.save_ticket(vars(ticket))


def edit_ticket(content):
    _id = content["_id"]
    ticket_data = db.get_ticket_by_id(_id)
    ticket = Ticket(**ticket_data)
    for k, v in ticket_data:
        ticket[k] = v
    db.save_ticket(vars(ticket))


def get_tickets_by_project(_id: int):
    tickets = db.get_tickets_by_project(_id)
    return [ticket for ticket in tickets if ticket["state"] != "resuelto"]


def get_ticket_by_id(_id: int):
    return db.get_ticket_by_id(_id)


def get_projects():
    projects_data = db.get_projects()
    projects = [Project(**data) for data in projects_data]
    return projects
