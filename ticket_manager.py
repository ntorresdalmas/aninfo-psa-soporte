from datetime import datetime, timedelta
from ticket import Ticket
from task import Task
import requests
import db


ALLOWED_STATES = ['en progreso soporte', 'escalado en ingeneria', 'esperando respuesta del cliente', 'resuelto'] #'abierto'
ALLOWED_TICKET_TYPES = ['consulta', 'error']
PRIORITY_AND_DAYS_TO_COMPLETE = {1: 7, 2: 90, 3: 180, 4: 365}   #{prioridad: maxima_cantidad_de_dias_limite}


def create_ticket(content):
    """
    Given a body we add 'creation_date', 'limit_date' and 'status' fields and store them in the db.
    """
    content['creation_date'] = datetime.now()
    content['limit_date'] = timedelta(days=PRIORITY_AND_DAYS_TO_COMPLETE[int(content['priority'])]) + content[
        'creation_date']
    content['status'] = 'abierto'
    ticket = Ticket(**content)
    db.save_ticket(vars(ticket))


def edit_ticket(content):
    """
    Given a body we add 'limit_date' if 'priority' has changed and store them in the db.
    """
    _id = content.pop('ticket_id', None)
    if content['priority']:
        content['limit_date'] = timedelta(days=PRIORITY_AND_DAYS_TO_COMPLETE[int(content['priority'])]) + \
                                datetime.strptime(get_ticket_by_id(_id)[0]['creation_date'], "%Y-%m-%d %H:%M:%S.%f")

    #TODO: task should be a list of dictionaries {'task_id' : 1.'task_name': 'tarea1'}
    db.edit_ticket(_id, content)

    #delete tasks related to tickets and create new matches between ticket & tasks
    #for task in content['tasks']:
    #   db.save_resolution({_id, task['task_id'], task['task_name'])


def get_tickets_by_project(_id: int):
    tickets = [Ticket(*row) for row in db.get_tickets_by_project(_id)]
    return [ticket.as_dict() for ticket in tickets if ticket.status != "resuelto"]


def get_all_tickets():
    tickets = [Ticket(*row) for row in db.get_all_tickets()]
    return [ticket.as_dict() for ticket in tickets if ticket.status != "resuelto"]


def get_all_tickets_main_data(filters):
    """
    Given or not the following filters 'status', 'priority' and returns list of tickets with main data
    :returns list of dictionaries { "id": , "name": , "status": , "priority": , "limit date": }
    """
    tickets = get_all_tickets()
    if filters:
        for k, v in filters.items():
            tickets = [ticket for ticket in tickets if ticket[k] == v]
    data = []
    for ticket in tickets:
        data.append({
            "id": ticket["id"],
            "name": ticket["name"],
            "status": ticket["status"],
            "priority": ticket["priority"],
            "limit date": ticket["limit_date"]
        })
    return data


def get_ticket_data(_id: int):
    """
    Given a ticket_id returns all related ticket data
    :returns dictionary { "id": , "name": , "description": , "status": , "priority": , "type": ,
     "task name": , "creation date": , "limit date": }
    """
    ticket = get_ticket_by_id(_id)[0]
    request = requests.get(f'https://squad6-backend.herokuapp.com/resources/{ticket["resource_id"]}')
    if request.status_code != 200:
        raise Exception("Problema al comunicarse con modulo proyectos")
    resource = request.json()
    tasks = []
    """
    all_tasks = get_all_tasks()
    ticket_tasks = db.get_tasks_by_ticket_id(_id)
    tasks = list()
    for task_detail in all_tasks:
        for task in ticket_tasks:
            if task_detail['codigo'] == task['task_id']:
                tasks.append({'codigo': task['task_id'], 'nombre': task_detail['nombre']})
    """
    return {
        "id": ticket["id"],
        "name": ticket["name"],
        "description": ticket["description"],
        "status": ticket["status"],
        "priority": ticket["priority"],
        "type": ticket["type"],
        "tasks name": tasks,
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
    project_request = get_projects()
    tasks = list()
    for project in project_request:
        task_request = requests.get(f'http://proyectopsa.herokuapp.com/proyectos/{project["codigo"]}/tarea')
        if task_request.status_code != 200:
            raise Exception("Problema al comunicarse con modulo proyectos")
        for task in task_request.json():
            if task['estado'] != 'finalizado':  #TODO: preguntar estados de tarea!
                tasks.append(task)
            else:
                db.delete_resolution_by_task(task['codigo'])
    return tasks


def get_tasks_from_ticket_id(_id):
    tasks = [Task(*row) for row in db.get_tasks_by_ticket_id(_id)]
    return [task.as_dict() for task in tasks]


def get_ticket_by_id(_id: int):
    tickets = [Ticket(*row) for row in db.get_ticket_by_id(_id)]
    return [ticket.as_dict() for ticket in tickets]


def get_projects():
    project_request = requests.get('http://proyectopsa.herokuapp.com/proyectos/')
    if project_request.status_code != 200:
        raise Exception("Problema al comunicarse con modulo proyectos")
    return list(filter(lambda x: x['estado'] != "finalizado", project_request.json()))
