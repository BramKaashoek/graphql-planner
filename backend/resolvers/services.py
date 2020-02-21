from backend.resolvers import types
from typing import List, Optional

Donatas = types.Person(id=1, name="Donatas")
GrapQL = types.Project(id=1, name="grapql")

def fetch_people() -> List[types.Person]:
    return [Donatas]

def fetch_projects() -> List[types.Project]:
    return [GrapQL]

def fetch_week_plannig(week_number: int) -> Optional[List[types.PersonPlanning]]:
    return [
            types.PersonPlanning(
                person=Donatas,
                week_number=1,
                week=[
                    types.Day(
                        weekday=types.Weekday.Monday,
                        items=[types.TimeAllocation(project=GrapQL, hours=1.0)]
                )
            ]
        )
    ]


def fetch_person_plan_for_week(week_number: int, person_id: int) -> types.PersonPlanning:
    return types.PersonPlanning(
                person=Donatas,
                week_number=1,
                week=[
                    types.Day(
                        weekday=types.Weekday.Monday,
                        items=[types.TimeAllocation(project=GrapQL, hours=1.0)]
                )
            ]
        )