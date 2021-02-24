from datetime import datetime, timedelta
from ticket import Ticket
from project import Project
import requests
import db


ALLOWED_STATES = ['en progreso soporte', 'escalado en ingeneria', 'esperando respuesta del cliente', 'resuelto'] #'abierto'
ALLOWED_TICKET_TYPES = ['consulta', 'error']
PRIORITY_AND_DAYS_TO_COMPLETE = {1: 7, 2: 90, 3: 180, 4: 365}   #{prioridad: maxima_cantidad_de_dias_limite}


def create_ticket(content):
    content['creation_date'] = datetime.now()
    content['limit_date'] = timedelta(days=PRIORITY_AND_DAYS_TO_COMPLETE[content['priority']]) + content['creation_date']
    content['status'] = 'abierto'
    #TODO: recibir project_id sacandolo del task desde el FE.
    ticket = Ticket(**content)
    db.save_ticket(vars(ticket))


def edit_ticket(content):
    _id = content.pop('ticket_id', None)
    if content['priority']:
        content['limit_date'] = timedelta(days=PRIORITY_AND_DAYS_TO_COMPLETE[content['priority']]) + get_ticket_by_id(_id)['creation_date']

    db.edit_ticket(_id, content)


def get_tickets_by_project(_id: int):
    tickets = [Ticket(*row) for row in db.get_tickets_by_project(_id)]
    return [ticket.as_dict() for ticket in tickets if ticket.status != "resuelto"]


def get_all_tickets():
    tickets = [Ticket(*row) for row in db.get_all_tickets()]
    return [ticket.as_dict() for ticket in tickets if ticket.status != "resuelto"]


def get_all_tickets_main_data(filters):
    tickets = get_all_tickets()
    #TODO recibir como filtro el id del proyecto y no el nombre, para filtrar mas facil
    if filters:
        for k, v in filters.items():
            tickets = [ticket for ticket in tickets if ticket[k] == v]
    request = requests.get('http://proyectopsa.herokuapp.com/proyectos/')
    if request.status_code != 200:
        raise Exception("Problema al comunicarse con modulo proyectos")
    projects = request.json()
    data = []

    for ticket in tickets:
        project_name = [project["nombre"] for project in projects\
                             if project["codigo"] == ticket["project_id"]]

        data.append({
            "name": ticket["name"],
            "status": ticket["status"],
            "priority": ticket["priority"],
            "project name": project_name[0] if project_name else None,
            "limit date": ticket["limit_date"]
        })

    return data




def get_ticket_by_id(_id: int):
    tickets = [Ticket(*row) for row in db.get_tickets_by_id(_id)]
    return [ticket.as_dict() for ticket in tickets]


def get_projects():
    projects_data = db.get_projects()
    projects = [Project(**data) for data in projects_data if data.estado != "finalizado"]
    return projects
