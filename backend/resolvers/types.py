from dataclasses import dataclass
from enum import Enum, auto
from typing import List

class Weekday(Enum):
    Monday = auto()
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()

@dataclass
class Person:
    id: int
    name: str
    
@dataclass
class Project:
    id: int
    name: str


@dataclass
class TimeAllocation:
    project: Project
    hours: float


@dataclass
class Day:
    weekday: Weekday
    items: List[TimeAllocation]

@dataclass
class PersonPlanning:
    person: Person
    week_number: int
    week: List[Day]