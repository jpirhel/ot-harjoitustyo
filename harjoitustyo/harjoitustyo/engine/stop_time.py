from dataclasses import dataclass, field

from .sql_object import SQLObject
from ..constant import ERROR_WEEKDAY


# pylint: disable=line-too-long
# reasoning: these are examples of lines from actual data, and they are long

# trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled,timepoint
# 1001_20230417_Ke_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1

# pylint: enable=line-too-long


@dataclass
class StopTime(SQLObject):
    """Holds information relating to a public transport stop time."""

    trip_id: str = field()
    arrival_time: str = field()
    departure_time: str = field()
    stop_id: str = field()
    stop_sequence: str = field()
    stop_headsign: str = field()
    pickup_type: str = field()
    drop_off_type: str = field()
    shape_dist_traveled: str = field()
    timepoint: str = field()

    route_short_name: str = field(init=False)

    @staticmethod
    def from_string(obj: str):
        """Initializes an instance of the StopTime class from data string.

        Returns:
             Instance of StopTime or None
        """

        parts = StopTime.clean_string(obj)

        trip_id = parts[0]

        if trip_id == "trip_id":
            return None

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

    def weekday(self):
        """Stop time weekday.

        Returns:
            0 for Monday through Friday,
            5 for Saturday,
            6 for Sunday
        """
        try:
            split = self.trip_id.split("_")
        except IndexError:
            return ERROR_WEEKDAY  # will not match today's weekday

        weekday = split[2].lower()

        # Monday to Friday

        if weekday in ("ma", "ti", "ke", "to", "pe"):
            return 0

        # Saturday

        if weekday == "la":
            return 5

        # Sunday

        if weekday == "su":
            return 6

        return ERROR_WEEKDAY

    def hour(self):
        """Stop time arrival hour.

        Returns:
            Hour as an integer
        """

        try:
            split = self.trip_id.split("_")
        except IndexError:
            return "00"

        time = split[4]

        hours = time[0:2]

        return int(hours)

    def minute(self):
        """Stop time arrival minute.

        Returns:
            Minute as an integer
        """

        try:
            split = self.trip_id.split("_")
        except ValueError:
            return "00"

        time = split[4]

        minutes = time[2:4]

        return int(minutes)

    def display_time(self):
        """Stop time in a format suitable for display.

        Returns:
            Displayable time as a string
        """

        try:
            split = self.trip_id.split("_")
        except ValueError:
            return "00:00"

        time = split[4]

        hours = time[0:2]
        minutes = time[2:4]

        if int(hours) >= 24:
            hours = f"0{int(hours) - 24}"

        return f"{hours}:{minutes}"

    @staticmethod
    def from_database(data):
        """Creates StopTime object from SQLite database row.

        Returns:
             Instance of class StopTime.
        """

        stop_time = StopTime(*data)

        return stop_time

    @staticmethod
    def from_database_with_route_short_name(data):
        """Creates StopTime object from SQLite database row.

        Adds a short route name to the object.

        Returns:
             Instance of class StopTime.
        """

        # last element of the tuple
        route_short_name = data[10]

        # remove last element of the data tuple
        data = data[:len(data) - 1]

        stop_time = StopTime.from_database(data)

        stop_time.route_short_name = route_short_name

        return stop_time
