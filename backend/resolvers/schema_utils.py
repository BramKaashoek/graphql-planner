from dataclasses import dataclass
from typing import Callable, Optional, Any, Dict, List, Tuple, Type
from enum import Enum
from ariadne import QueryType, make_executable_schema, load_schema_from_path, EnumType
from ariadne.asgi import GraphQL

# Type aliases
AnyMap = Dict[str, Any]

@dataclass
class Resolver:
    name: str
    function: Callable
    param_parser: Optional[Callable[[Any, AnyMap, AnyMap], AnyMap]] = None

    def __call__(self, parent: Optional[Any], info: AnyMap, **kwargs: AnyMap):
        annotations = dict(self.function.__annotations__)
        if self.param_parser:
            parameters = self.param_parser(parent, info, **kwargs)
        else:
            base_params = {key: (kwargs.get(key), _type) for key, _type in annotations.items() if key in kwargs}
            apply_type = lambda val, t: t(**val) if isinstance(val, dict) else t(val)
            parameters = {
                key: apply_type(*arg) for key, arg in base_params.items()
            }
        return self.function(**parameters)


def construct(resolvers: List[Resolver], enum_mappings: List[Tuple[str, Type[Enum]]], schema_path: str, debug: bool = False) -> GraphQL:
    query = QueryType()
    query._resolvers = {r.name: r for r in resolvers}
    enum_types = [EnumType(*x) for x in enum_mappings]
    schema = make_executable_schema(
        load_schema_from_path(schema_path),
        *enum_types,
        query
    )
    return GraphQL(schema=schema, debug=debug)
