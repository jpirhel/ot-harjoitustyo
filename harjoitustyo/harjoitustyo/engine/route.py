from dataclasses import dataclass

from .sql_object import SQLObject


# pylint: disable=line-too-long
# reasoning: these are examples of lines from actual data, and they are long

# format of data:
# route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url
# 1001,HSL,1,Eira - Töölö - Sörnäinen (M) - Vallila,,0,http://aikataulut.hsl.fi/linjat/fi/h1_1a.html

# pylint: enable=line-too-long


@dataclass
class Route(SQLObject):
    """Holds information relating to a public transport route"""

    route_id: str
    agency_id: str
    route_short_name: str
    route_long_name: str
    route_desc: str
    route_type: str
    route_url: str

    @staticmethod
    def from_string(obj: str):
        """Initializes an instance of the Route class based on data string

        Returns:
             an instance of the class Route or None
        """

        # noinspection DuplicatedCode
        parts = Route.clean_string(obj)

        route_id = parts[0]

        # header
        if route_id == "route_id":
            return None

        agency_id = parts[1]
        route_short_name = parts[2]
        route_long_name = parts[3]
        route_desc = parts[4]
        route_type = parts[5]
        route_url = parts[6]

        obj = Route(
            route_id,
            agency_id,
            route_short_name,
            route_long_name,
            route_desc,
            route_type,
            route_url
        )

        return obj
