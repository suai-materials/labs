from dataclasses import dataclass


@dataclass
class Author:
    last_name: str
    first_name: str
    second_name: str = ""
