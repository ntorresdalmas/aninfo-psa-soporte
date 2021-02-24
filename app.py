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


@app.route('/tickets_main_data', methods=['POST'])
def get_all_tickets_main_data():
    """
    Exclusive use for front app
    """
    filters = request.json
    return json.dumps(ticket_manager.get_all_tickets_main_data(filters))


@app.route('/<project_id>/tickets', methods=['GET'])
def get_tickets(project_id):
    """
    only shows the ones with state != resuelto
    """
    return json.dumps(ticket_manager.get_tickets_by_project(project_id))


@app.route('/tickets', methods=["GET"])
def get_all_tickets():
    return json.dumps(ticket_manager.get_all_tickets())


@app.route('/<project_id>/createTicket', methods=['POST'])
def create_ticket(project_id):
    content = request.json
    ticket_manager.create_ticket(content)
    return {"status": 200,
            "ticket_id": 1}


@app.route('/<project_id>/editTicket', methods=['POST'])
def edit_ticket(project_id):
    content = request.json
    ticket_manager.edit_ticket(content)
    return {"status": 200}


if __name__ == "__main__":
  app.run()