from fastapi import FastAPI
from ariadne.asgi import GraphQL
from schema import schema
from db import db
from db import models


models.Base.metadata.create_all(bind=db.engine)

def seed():
    session = db.Session()
    # import pdb; pdb.set_trace()
    bram = models.Person(name="Bram")
    session.add(bram)
    dtc = models.Project(name="dtc")
    session.add(dtc)
    session.commit()

# seed()

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request, call_next):
    request.state.db = db.Session()
    response = await call_next(request)
    request.state.db.close()
    return response

app.mount("/graphql", GraphQL(schema, debug=True))

