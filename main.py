from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL

app = FastAPI()

type_defs = load_schema_from_path("schema.graphql")
query = QueryType()

@query.field("people")
def resolve_hello(*_):
    return []

@query.field("projects")
def resolve_projects(*_):
    return []

@query.field("planning")
def resolve_planning(*_):
    return []

@query.field("weekPlanning")
def resolve_week_planning(*_):
    return []


# Create executable schema instance
schema = make_executable_schema(type_defs, query)

app.mount("/graphql", GraphQL(schema, debug=True))