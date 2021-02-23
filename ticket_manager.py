from datetime import datetime
from ticket import Ticket
from project import Project
import db


ALLOWED_STATES = ['abierto', 'en progreso soporte', 'escalado en ingeneria', 'esperando respuesta del cliente', 'resuelto']
ALLOWED_TICKET_TYPES = ['consulta', 'error']
PRIORITY_AND_DAYS_TO_COMPLETE = {1 : 7, 2 : 90, 3 : 180, 4 : 365}   #{prioridad: maxima_cantidad_de_dias_limite}


def create_ticket(content):
    ticket = Ticket(**content)
    db.save_ticket(vars(ticket))


def edit_ticket(content):
    _id = content.pop('ticket_id', None)
    #TODO: escribir piola
    #if ticket.priority:
    #    content['limit_date'] = PRIORITY_AND_DAYS_TO_COMPLETE[ticket.priority] + ticket.creation_date
    #
    #if ticket.task_id:
    #    # pegarle a la API de get_tareas y get_proyectos y obtener de la tarea el recurso_asignado y codigoProyecto
    #    tareas = get_tareas()
    #    tarea = tareas[ticket.task_id]
    #    content['project_id'] = tarea.recursoAsignado
    #    content['resource_id'] = tarea.codigoProyecto

    db.edit_ticket(_id, content)


def get_tickets_by_project(_id: int):
    tickets = [Ticket(*row) for row in db.get_tickets_by_project(_id)]
    return [ticket.as_dict() for ticket in tickets if ticket.status != "resuelto"]


def get_ticket_by_id(_id: int):
    tickets = [Ticket(*row) for row in db.get_tickets_by_id(_id)]
    return [ticket.as_dict() for ticket in tickets]


def get_projects():
    projects_data = db.get_projects()
    projects = [Project(**data) for data in projects_data if data.estado != "finalizado"]
    return projects
