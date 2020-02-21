from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from resolvers.people.people import resolve_people

app = FastAPI()

type_defs = load_schema_from_path("schema.graphql")
query = QueryType()


@query.field("planning")
def resolve_planning(*_):
    return []

@query.field("weekPlanning")
def resolve_week_planning(*_):
    return []


# Bind resolvers
query.set_field("people", resolve_people)
query.set_field("projects", resolve_projects)

# Create executable schema instance
schema = make_executable_schema(type_defs, query)

app.mount("/graphql", GraphQL(schema, debug=True))