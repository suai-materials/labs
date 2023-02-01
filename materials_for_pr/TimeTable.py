import datetime
from dataclasses import dataclass

@dataclass
class TimeTable:
    performance_id: int
    scene_id: int
    datetime_start: datetime.datetime
    description: str = ""