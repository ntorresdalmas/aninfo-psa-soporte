from dataclasses import dataclass

@dataclass
class Task:
    code: int
    name: str
    status: str
    description: str
