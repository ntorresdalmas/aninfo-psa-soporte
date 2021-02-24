from flask import Flask, request, jsonify
from datetime import datetime
from ticket import Ticket
import ticket_manager
import json

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def home():
    return "<h1>PSA - soporte</h1><p>Main Menu</p>"


@app.route('/tickets_main_data', methods=['POST'])
@cross_origin()
def get_all_tickets_main_data():
    """
    Exclusive use for front app
    """
    filters = request.json
    return json.dumps(ticket_manager.get_all_tickets_main_data(filters))


@app.route('/ticket_data/<ticket_id>', methods=['GET'])
@cross_origin()
def get_ticket_data(ticket_id):
    """
    Exclusive use for front app
    """
    return json.dumps(ticket_manager.get_ticket_data(ticket_id))


@app.route('/<project_id>/tickets', methods=['GET'])
@cross_origin()
def get_tickets(project_id):
    """
    only shows the ones with state != resuelto
    """
    return json.dumps(ticket_manager.get_tickets_by_project(project_id))


@app.route('/tickets', methods=["GET"])
@cross_origin()
def get_all_tickets():
    return json.dumps(ticket_manager.get_all_tickets())


@app.route('/create_ticket', methods=['POST'])
@cross_origin()
def create_ticket():
    content = request.json
    print(content)
    ticket_manager.create_ticket(content)
    return {"status": 200,
            "ticket_id": 1}


@app.route('/edit_ticket', methods=['POST'])
@cross_origin()
def edit_ticket():
    content = request.json
    print(content)
    ticket_manager.edit_ticket(content)
    return {"status": 200}


if __name__ == "__main__":
  app.run()