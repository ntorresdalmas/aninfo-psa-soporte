from flask import Flask, request
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


@app.route('/tasks', methods=["GET"])
@cross_origin()
def get_all_tasks():
    """
    shows all the tasks from all projects
    """
    return json.dumps(ticket_manager.get_all_tasks())


@app.route('/tasks_by_id', methods=["POST"])
@cross_origin()
def get_tasks_by_id():
    """
    shows all the tasks from a ticket id
    """

    ticket_id = request.json['ticket_id']
    return json.dumps(ticket_manager.get_tasks_from_ticket_id(ticket_id))



@app.route('/tickets_main_data', methods=['POST'])
@cross_origin()
def get_all_tickets_main_data():
    """
    Exclusive use for front app
    """
    filters = request.json
    return json.dumps(ticket_manager.get_all_tickets_main_data(filters))


@app.route('/ticket_data', methods=['POST'])
@cross_origin()
def get_ticket_data():
    """
    Exclusive use for front app
    """
    ticket_id = request.json['ticket_id']
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
    """
    shows all the tickets
    """
    return json.dumps(ticket_manager.get_all_tickets())


@app.route('/create_ticket', methods=['POST'])
@cross_origin()
def create_ticket():
    """
    body:
    {
    "resource_id": int
    "name": str
    "type": str
    "description": str
    "priority": int
    }
    """
    content = request.json
    print(content)
    ticket_manager.create_ticket(content)
    return {"status": 200,
            "ticket_id": 1}


@app.route('/edit_ticket', methods=['POST'])
@cross_origin()
def edit_ticket():
    """
    body:
    {
    "resource_id": int
    "status": str
    "description": str
    "priority": int
    }
    """
    content = request.json
    print(content)
    ticket_manager.edit_ticket(content)
    return {"status": 200}


@app.route('/edit_tasks_ticket', methods=['POST'])
@cross_origin()
def edit_tasks_ticket():
    """
    body:
    {
    "ticket_id": int,
    "tasks" : [{
    "task_id": int,
    "task_name": str
    }]
    }
    """
    content = request.json
    ticket_manager.edit_tasks_ticket(content)
    return {"status": 200}


if __name__ == "__main__":
  app.run()