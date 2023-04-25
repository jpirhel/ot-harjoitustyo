import logging

from harjoitustyo.engine.data.reader import Reader


class Handler:
    """Takes input from control panel and map, and sends commands to control panel and map"""

    def __init__(self, control, map_):
        self._log = logging.getLogger("Handler")

        self._control = control
        self._map = map_

        self._reader = Reader()

        stops = self._reader.read_stops()

        for stop in stops:
            self._map.add_stop_marker(stop)

    def handle(self, name=None, data=None, data2=None):
        print("Handler.handle, name=%s, data=%s, data2=%s" %
              (name, data, data2), flush=True)

        if name is None:
            self._log.error("Failed to handle name: %s, data: %s", name, data)

        if name == "map_home":
            self._handle_map_home()

        if name == "map_plus":
            self._handle_map_plus()

        if name == "map_minus":
            self._handle_map_minus()

        if name == "map_marker_clicked":
            self._handle_map_marker_clicked(data, data2)

    def _handle_map_home(self):
        self._map.reset_map_position()

    def _handle_map_plus(self):
        self._map.zoom_in()

    def _handle_map_minus(self):
        self._map.zoom_out()

    def _handle_map_marker_clicked(self, marker, stop):
        print(
            f"HANDLE_MAP_MARKER_CLICKED, marker: {marker}, stop: {stop}", flush=True)

        self._control.stop_info(stop)

        # new_text = marker.text + "*"
        # marker.set_text(new_text)
