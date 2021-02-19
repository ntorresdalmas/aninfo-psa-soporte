from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ticket:
    id: int
    project_id: int
    resource_id: int
    task_id: int
    name: str
    status: str
    type: str
    description: str
    priority: int
    creation_date: datetime
    limit_date: datetime

    def as_dict(self):
        ticket_as_dict = vars(self)
        ticket_as_dict["creation_date"] = str(ticket_as_dict["creation_date"])
        ticket_as_dict["limit_date"] = str(ticket_as_dict["limit_date"])
        return ticket_as_dict

