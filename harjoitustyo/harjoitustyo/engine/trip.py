from dataclasses import dataclass

from .sql_object import SQLObject


# pylint: disable=line-too-long
# reasoning: these are examples of lines from actual data, and they are long

# format of data:
# route_id,service_id,trip_id,trip_headsign,direction_id,shape_id,wheelchair_accessible,bikes_allowed,max_delay
# 1001,1001_20230417_20230531_Ke,1001_20230417_Ke_1_0540,"Vallila",0,1001_20230306_1,1,2,3

# pylint: enable=line-too-long


# noinspection DuplicatedCode
@dataclass
class Trip(SQLObject):
    """Holds information relating to a public transport trip."""

    route_id: str
    service_id: str
    trip_id: str
    trip_headsign: str
    direction_id: str
    shape_id: str
    wheelchair_accessible: str
    bikes_allowed: str
    max_delay: str

    @staticmethod
    def from_string(obj: str):
        """Initializes an instance of the Trip class from data string.

        Returns:
             Instance of Trip or None
        """

        parts = Trip.clean_string(obj)

        route_id = parts[0]

        # header
        if route_id == "route_id":
            return None

        service_id = parts[1]
        trip_id = parts[2]
        trip_headsign = parts[3]
        direction_id = parts[4]
        shape_id = parts[5]
        wheelchair_accessible = parts[6]
        bikes_allowed = parts[6]
        max_delay = parts[7]

        obj = Trip(
            route_id,
            service_id,
            trip_id,
            trip_headsign,
            direction_id,
            shape_id,
            wheelchair_accessible,
            bikes_allowed,
            max_delay
        )

        return obj
