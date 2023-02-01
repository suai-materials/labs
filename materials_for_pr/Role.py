from dataclasses import dataclass


@dataclass
class Role:
    name: str
    performance_id: int
    description: str = ""
