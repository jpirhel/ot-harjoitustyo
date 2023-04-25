from dataclasses import dataclass

from .sql_object import SQLObject

# pylint: disable=line-too-long
# reasoning: these are examples of lines from actual data, and they are long

# trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled,timepoint
# 1001_20230417_Ke_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1

# pylint: enable=line-too-long


@dataclass
class StopTime(SQLObject):
    """Holds information relating to a public transport stop time"""

    trip_id: str
    arrival_time: str
    departure_time: str
    stop_id: str
    stop_sequence: str
    stop_headsign: str
    pickup_type: str
    drop_off_type: str
    shape_dist_traveled: str
    timepoint: str

    @staticmethod
    def from_string(obj: str):
        parts = StopTime.clean_string(obj)

        trip_id = parts[0]
        arrival_time = parts[1]
        departure_time = parts[2]
        stop_id = parts[3]
        stop_sequence = parts[4]
        stop_headsign = parts[5]
        pickup_type = parts[6]
        drop_off_type = parts[7]
        shape_dist_traveled = parts[8]
        timepoint = parts[9]

        obj = StopTime(
            trip_id,
            arrival_time,
            departure_time,
            stop_id,
            stop_sequence,
            stop_headsign,
            pickup_type,
            drop_off_type,
            shape_dist_traveled,
            timepoint
        )

        return obj
