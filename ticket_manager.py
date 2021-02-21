from datetime import datetime
from ticket import Ticket
from project import Project
import db


ALLOWED_STATES = ['abierto', 'en progreso soporte', 'escalado en ingeneria', 'esperando respuesta del cliente', 'resuelto']
ALLOWED_TICKET_TYPES = ['consulta', 'error']
PRIORITY_AND_DAYS_TO_COMPLETE = {1 : 7, 2 : 90, 3 : 180, 4 : 365}   #{prioridad: axima_cantidad_de_dias_limite}


def create_ticket(content):
    ticket = Ticket(**content)
    db.save_ticket(vars(ticket))


def edit_ticket(content):
    _id = content.pop('ticket_id', None)
    db.edit_ticket(_id, content)


def get_tickets_by_project(_id: int):
    tickets = [Ticket(*row) for row in db.get_tickets_by_project(_id)]
    return [ticket.as_dict() for ticket in tickets if ticket.status != "resuelto"]


def get_ticket_by_id(_id: int):
    tickets = [Ticket(*row) for row in db.get_tickets_by_id(_id)]
    return [ticket.as_dict() for ticket in tickets]


def get_projects():
    projects_data = db.get_projects()
    projects = [Project(**data) for data in projects_data]
    return projects
