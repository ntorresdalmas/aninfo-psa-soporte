from dataclasses import dataclass

@dataclass
class Task:
    ticket_id: int
    task_id: int
    name: str

    def as_dict(self):
        return vars(self)