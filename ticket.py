from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ticket:
    id: int
    resource_id: int
    name: str
    status: str
    type: str
    description: str
    priority: int
    creation_date: datetime
    limit_date: datetime

    def as_dict(self):
        ticket_as_dict = vars(self)
        ticket_as_dict["creation_date"] = datetime.strftime(ticket_as_dict["creation_date"], "%Y-%m-%d %H:%M:%S")
        ticket_as_dict["limit_date"] = datetime.strftime(ticket_as_dict["limit_date"], "%Y-%m-%d %H:%M:%S")
        return ticket_as_dict
