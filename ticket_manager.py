from datetime import datetime, timedelta
from ticket import Ticket
from project import Project
import requests
import db


ALLOWED_STATES = ['en progreso soporte', 'escalado en ingeneria', 'esperando respuesta del cliente', 'resuelto'] #'abierto'
ALLOWED_TICKET_TYPES = ['consulta', 'error']
PRIORITY_AND_DAYS_TO_COMPLETE = {1: 7, 2: 90, 3: 180, 4: 365}   #{prioridad: maxima_cantidad_de_dias_limite}


def create_ticket(content):
    """
    Given a body we add 'creation_date', 'limit_date', 'status' and 'project_id' fields and store them in the db.
    """
    projects = get_projects()
    project_id = None
    for project in projects:
        request = requests.get(f'http://proyectopsa.herokuapp.com/proyectos/{project["codigo"]}/tarea/{content["task_id"]}')
        if 'tarea' in request.json():
            project_id = project['codigo']

    content['creation_date'] = datetime.now()
    content['limit_date'] = timedelta(days=PRIORITY_AND_DAYS_TO_COMPLETE[int(content['priority'])]) + content[
        'creation_date']
    content['project_id'] = project_id
    content['status'] = 'abierto'
    ticket = Ticket(**content)
    db.save_ticket(vars(ticket))


def edit_ticket(content):
    """
    Given a body we add 'limit_date' if 'priority' has changed and store them in the db.
    """
    _id = content.pop('ticket_id', None)
    if content['priority']:
        content['limit_date'] = timedelta(days=PRIORITY_AND_DAYS_TO_COMPLETE[int(content['priority'])]) + datetime.strptime(get_ticket_by_id(_id)[0]['creation_date'], "%Y-%m-%d %H:%M:%S")

    db.edit_ticket(_id, content)


def get_tickets_by_project(_id: int):
    tickets = [Ticket(*row) for row in db.get_tickets_by_project(_id)]
    # TODO: preguntar si un ticket una vez que esta resuelto se sigue mostrando en el FRONT
    return [ticket.as_dict() for ticket in tickets if ticket.status != "resuelto"]


def get_all_tickets():
    tickets = [Ticket(*row) for row in db.get_all_tickets()]
    #TODO: preguntar si un ticket una vez que esta resuelto se sigue mostrando en el FRONT
    return [ticket.as_dict() for ticket in tickets if ticket.status != "resuelto"]


def get_all_tickets_main_data(filters):
    """
    Given or not the following filters 'status', 'priority' and 'project_id' returns list of tickets with main data
    :returns list of dictionaries { "id": , "name": , "status": , "priority": , "project name": , "limit date": }
    """
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
            "id": ticket["id"],
            "name": ticket["name"],
            "status": ticket["status"],
            "priority": ticket["priority"],
            "project name": project_name[0] if project_name else None,
            "limit date": ticket["limit_date"]
        })

    return data


def get_ticket_data(_id: int):
    """
    Given a ticket_id returns all related ticket data
    :returns dictionary { "id": , "name": , "description": , "status": , "priority": , "type": , "project name": ,
     "task name": , "task description" , "creation date": , "limit date": }
    """
    ticket = get_ticket_by_id(_id)[0]

    request = requests.get(f'http://proyectopsa.herokuapp.com/proyectos/{ticket["project_id"]}/tarea/{ticket["task_id"]}')

    if request.status_code != 200:
        raise Exception("Problema al comunicarse con modulo proyectos")
    task = request.json()['tarea']

    request = requests.get(f'https://squad6-backend.herokuapp.com/resources/{ticket["resource_id"]}')
    if request.status_code != 200:
        raise Exception("Problema al comunicarse con modulo proyectos")
    resource = request.json()

    return {
        "id": ticket["id"],
        "name": ticket["name"],
        "description": ticket["description"],
        "status": ticket["status"],
        "priority": ticket["priority"],
        "type": ticket["type"],
        "project name": task["nombreProyecto"],
        "task name": task["nombre"],
        "task description": task["descripcion"],
        "resource id": resource["legajo"],
        "resource name": f"{resource['Nombre']} {resource['Apellido']}",
        "creation date": ticket["creation_date"],
        "limit date": ticket["limit_date"]
    }


def get_all_tasks():
    """
    Get all the task from all projects
    :return: list of dictionarys: {'codigo': 8, 'estado': 'iniciado', 'nombre': 'agregar recursos'}
    """
    project_request = requests.get('http://proyectopsa.herokuapp.com/proyectos/')
    if project_request.status_code != 200:
        raise Exception("Problema al comunicarse con modulo proyectos")
    tasks = list()
    for project in project_request.json():
        task_request = requests.get(f'http://proyectopsa.herokuapp.com/proyectos/{project["codigo"]}/tarea')
        if project_request.status_code != 200:
            raise Exception("Problema al comunicarse con modulo proyectos")
        tasks.extend(task_request.json())
    return tasks


def get_ticket_by_id(_id: int):
    tickets = [Ticket(*row) for row in db.get_ticket_by_id(_id)]
    return [ticket.as_dict() for ticket in tickets]


def get_projects():
    project_request = requests.get('http://proyectopsa.herokuapp.com/proyectos/')
    if project_request.status_code != 200:
        raise Exception("Problema al comunicarse con modulo proyectos")

    return list(filter(lambda x: x['estado'] != "finalizado", project_request.json()))
