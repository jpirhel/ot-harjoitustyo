from dataclasses import dataclass

from .sql_object import SQLObject


# pylint: disable=line-too-long
# reasoning: these are examples of lines from actual data, and they are long

# format of data:
# stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station,wheelchair_boarding,platform_code,vehicle_type
# 1010107,H2014,"Meritullinkatu","Liisankatu",60.174128,24.955551,A,http://aikataulut.hsl.fi/pysakit/fi/1010107.html,0, ,2, ,3

# pylint: enable=line-too-long

# Example of fields:
# stop_id = 1230109
# stop_code = "H3037"
# stop_name = "Kumpulan kampus"
# stop_desc = "Hämeentie"
# stop_lat = 60.203120
# stop_lon = 24.967300
# zone_id = "A"
# stop_url = "http://aikataulut.hsl.fi/pysakit/fi/1230109.html"
# location_type = 0
# parent_station = None
# wheelchair_boarding = 2
# platform_code = None
# vehicle_type = 3


@dataclass
class Stop(SQLObject):
    """Holds information relating to a public transport Stop."""

    stop_id: int
    stop_code: str
    stop_name: str
    stop_desc: str
    stop_lat: float
    stop_lon: float
    zone_id: str
    stop_url: str
    location_type: int | None
    parent_station: int | None
    wheelchair_boarding: int | None
    platform_code: str | None
    vehicle_type: int | None

    @staticmethod
    def from_string(obj: str):
        """Creates a Stop object from stop data.

        Returns: Instance of class Stop or None.
        """

        parts = Stop.clean_string(obj)

        try:
            stop_id = int(parts[0])
        except ValueError:
            return None

        stop_code = parts[1]
        stop_name = parts[2]
        stop_desc = parts[3]
        stop_lat = float(parts[4])
        stop_lon = float(parts[5])
        zone_id = parts[6]
        stop_url = parts[7]

        # pylint: disable=consider-using-ternary,simplify-boolean-expression
        # reasoning: couldn't be bothered to simplify these, unfortunately

        location_type = parts[8] and int(parts[8]) or None
        parent_station = parts[9] and int(parts[9]) or None
        wheelchair_boarding = parts[10] and int(parts[10]) or None
        platform_code = parts[11] and str(parts[11]) or None
        vehicle_type = parts[12] and int(parts[12]) or None

        # pylint: enable=consider-using-ternary,simplify-boolean-expression

        obj = Stop(
            stop_id,
            stop_code,
            stop_name,
            stop_desc,
            stop_lat,
            stop_lon,
            zone_id,
            stop_url,
            location_type,
            parent_station,
            wheelchair_boarding,
            platform_code,
            vehicle_type
        )

        return obj

    @staticmethod
    def clean_string(data_string: str):
        """Cleans up stop line data.

        Returns: List of cleaned data parts.
        """

        parts = data_string.split(",")

        cleaned = []

        # Quick and dirty fix for stop names with commas

        if len(parts) == 14:
            tmp = parts
            parts[0] = tmp[0]
            parts[1] = tmp[1]
            parts[2] = f"{tmp[2]},{tmp[3]}"
            parts[3] = tmp[4]
            parts[4] = tmp[5]
            parts[5] = tmp[6]
            parts[7] = tmp[8]
            parts[8] = tmp[9]
            parts[9] = tmp[10]
            parts[10] = tmp[11]
            parts[11] = tmp[12]
            parts[12] = tmp[13]

        for part in parts:
            cleaned.append(part.strip().replace('"', ''))

        return cleaned

    @staticmethod
    def from_database(data):
        """Creates Stop object from SQLite database row.

        Returns: Instance of class Stop.
        """

        stop = Stop(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
            data[6],
            data[7],
            data[8],
            data[9],
            data[10],
            data[11],
            data[12],
        )

        return stop

    @property
    def lat(self):
        """Stop latitude as a float"""

        return float(self.stop_lat)

    @property
    def lon(self):
        """Stop longitude as a float"""

        return float(self.stop_lon)

    def coord(self):
        """Stop coordinates as a tuple"""

        return self.stop_lat, self.stop_lon

    def corrected_stop_url(self):
        """Returns corrected stop URL for opening stop info on HSL.fi website.

        Stop.stop_url included in the doesn't point to a working URL, the URL generated
        by this function is correct at the time of writing the function.

        Returns: URL to Stop timetable on HSL.fi .
        """

        return f"https://reittiopas.hsl.fi/pysakit/HSL%3A{self.stop_id}"
