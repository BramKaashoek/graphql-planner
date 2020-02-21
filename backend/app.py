from fastapi import FastAPI
from backend.resolvers.schema_utils import construct

graphql_route = construct(
    resolvers=[],
    enum_mappings=[],
    schema_path="schema.graphql"
)

app = FastAPI("/", graphql_route)