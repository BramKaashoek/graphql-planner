from ariadne import QueryType, make_executable_schema, load_schema_from_path
from resolvers.people.people import resolve_people
from resolvers.projects.projects import resolve_projects

type_defs = load_schema_from_path("typedefs.graphql")
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