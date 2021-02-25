from dataclasses import dataclass
from datetime import datetime


@dataclass
class Project:
    _id: int
    nombre: str
    estado: str
