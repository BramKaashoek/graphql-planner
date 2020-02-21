from db import models

def resolve_people(obj, info):
    db = info.context['request']['state']['db']
    people =  db.query(models.Person).all()
    return people
