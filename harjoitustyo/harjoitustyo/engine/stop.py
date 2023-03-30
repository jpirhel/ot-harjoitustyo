from dataclasses import dataclass

# format of data:
# stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station,wheelchair_boarding,platform_code,vehicle_type
# 1010107,H2014,"Meritullinkatu","Liisankatu",60.174128,24.955551,A,http://aikataulut.hsl.fi/pysakit/fi/1010107.html,0, ,2, ,3

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
class Stop:
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
    platform_code: int | None
    vehicle_type: int | None

    @staticmethod
    def from_string(s: str):
        # NOTE: no error handling code implemented yet

        parts = s.split(",")

        cleaned = []

        for part in parts:
            c = part.strip().replace('"', '')
            cleaned.append(c)

        parts = cleaned

        stop_id = int(parts[0])
        stop_code = parts[1]
        stop_name = parts[2]
        stop_desc = parts[3]
        stop_lat = float(parts[4])
        stop_lon = float(parts[5])
        zone_id = parts[6]
        stop_url = parts[7]
        location_type = parts[8] and int(parts[8]) or None
        parent_station = parts[9] and int(parts[9]) or None
        wheelchair_boarding = parts[10] and int(parts[10]) or None
        platform_code = parts[11] and int(parts[11]) or None
        vehicle_type = parts[12] and int(parts[12]) or None

        s = Stop(
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

        return s
