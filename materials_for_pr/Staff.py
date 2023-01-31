from dataclasses import dataclass


@dataclass
class Staff:
    last_name: str
    first_name: str
    second_name: str
    position_id: int = -1
