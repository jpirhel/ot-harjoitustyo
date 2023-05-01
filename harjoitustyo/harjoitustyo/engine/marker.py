class Marker:
    """Holds information relating to a map marker, including object pointed to"""

    def __init__(self, name, lat, lon, obj=None):
        """Initializes the Marker instance.

        Args:
            name: Name of the marker (displayed on the map)
            lat: latitude of the marker
            lon: longitude of the marker
            obj: object pointed to by the marker, used in callbacks
        """

        self.name = name
        self.lat = lat
        self.lon = lon
        self.obj = obj
