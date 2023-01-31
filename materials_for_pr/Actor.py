from dataclasses import dataclass
from datetime import date


@dataclass
class Actor:
    last_name: str
    first_name: str
    second_name: str
    date_of_birth: date
    bio: str = ''
