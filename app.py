from flask import Flask, request, jsonify
from datetime import datetime
from ticket import Ticket
import ticket_manager
import json

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>PSA - soporte</h1><p>Main Menu</p>"

@app.route('/projects/', methods=['GET'])
def get_projects():
    proj_list = list()
    return proj_list

@app.route('/<project_id>/tickets', methods=['GET'])
def get_tickets(project_id):
    """
    only shows the ones with state != resuelto
    """
    return ticket_manager.get_tickets_by_project(project_id)


@app.route('/<project_id>/createTicket', methods=['POST'])
def create_ticket(project_id):
    content = request.json
    ticket_manager.create_ticket(content)
    return 200


@app.route('/<project_id>/editTicket', methods=['POST'])
def edit_ticket(project_id):
    content = request.json
    ticket_manager.edit_ticket(content)
    return 200




app.run()