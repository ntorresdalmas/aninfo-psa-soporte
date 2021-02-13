from flask import Flask, request, jsonify
import json

app = Flask(__name__)
app.config["DEBUG"] = True

states = ['abierto', 'en progreso soporte', 'escalado en ingeneria', 'esperando respuesta del cliente', 'resuelto']
ticket_types = ['consulta','error']

@app.route('/', methods=['GET'])
def home():
    return "<h1>PSA - soporte</h1><p>Main Menu</p>"

@app.route('/projects/', methods=['GET'])
def getProjects():
    proj_list = list()
    return proj_list

@app.route('/<project_id>/tickets', methods=['GET'])
def getTickets(project_id):
    """
    only shows the ones with state != resuelto
    """
    ticket_list = list()
    return ticket_list

@app.route('/<project_id>/createTicket', methods=['POST'])
def createTicket(project_id):
    client_id = ''  #???esto entra al final???
    task_id = ''    #???
    resource_id = ''    #???
    body = {
        'project_id': project_id,
        'client_id': client_id,
        'task_id': task_id,
        'resource_id': resource_id,
        'id': 1,
        'state': 'en progreso soporte',
        'ticket_type': 'error',
        'description': 'bla bla bla',
        'priority': 3,
        'created_date': '12-12-12',
        'limit_date': '12-12-12'
    }
    return body

@app.route('/<project_id>/editTicket', methods=['POST'])
def editTicket(project_id):
    client_id = ''  #???esto entra al final???
    task_id = ''    #???
    resource_id = ''    #???
    body = {
        'project_id': project_id,
        'client_id': client_id,
        'task_id': task_id,
        'resource_id': resource_id,
        'id': 1,
        'state': 'en progreso soporte',
        'ticket_type': 'error',
        'description': 'bla bla bla',
        'priority': 3,
        'created_date': '12-12-12',
        'limit_date': '12-12-12'
    }
    return body




app.run()