from dataclasses import dataclass


@dataclass
class Scene:
    id: int
    name: str
    address: str = ''
    description: str = ''
