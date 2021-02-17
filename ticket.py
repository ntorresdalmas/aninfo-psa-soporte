from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ticket:
    project_id: int
    client_id: int
    task_id: int
    resource_id: int
    id: int
    status: str
    ticket_type: str
    description: str
    priority: int
    created_date: datetime
    limit_date: datetime



