from dataclasses import dataclass

@dataclass
class PerformanceType:
    id: int
    name: str
    peculiarities: str = ""