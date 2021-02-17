from dataclasses import dataclass

@dataclass
class Task:
    code: str
    status: str
    description: str
    assigned_resource: str
    estimated_effort: int
    real_effort: int

