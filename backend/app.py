from fastapi import FastAPI
from backend.resolvers.schema_utils import construct, Resolver
from backend.resolvers import services
from backend.resolvers import types

graphql_route = construct(
    resolvers=[
        Resolver(name="people", function=services.fetch_people),
        Resolver(name="projects", function=services.fetch_projects),
        Resolver(name="weekPlanning", function=services.fetch_week_plannig),
        Resolver(name="personWeekPlanning", function=services.fetch_person_plan_for_week)
    ],
    enum_mappings=[("Weekday", types.Weekday)],
    schema_path="schema.graphql"
)
app = FastAPI()
app.add_route("/", graphql_route)