class Marker:
    def __init__(self, name, lat, lon, obj=None):
        """Holds information relating to a map marker, including object pointed to"""

        self.name = name
        self.lat = lat
        self.lon = lon
        self.obj = obj
