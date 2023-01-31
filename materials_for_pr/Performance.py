from dataclasses import dataclass


@dataclass
class Performance:
    name: str
    type_id: int
    acts: int
    duration: int
