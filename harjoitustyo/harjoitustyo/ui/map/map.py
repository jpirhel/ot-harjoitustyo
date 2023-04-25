import logging

import PIL.Image
import PIL.ImageTk

import tkinter as tk

import tkintermapview

from harjoitustyo.constant import KUMPULA_LAT, KUMPULA_LON, ZOOM_DEFAULT, ZOOM_MIN, ZOOM_MAX


class Map:
    def __init__(self, container):
        self._container = container
        self._handler = None

        self._log = logging.getLogger("App.Ui.Map")

        self._lat = KUMPULA_LAT
        self._lon = KUMPULA_LON
        self._zoom = ZOOM_DEFAULT

        self._markers = dict()

        self._map = self._init_map_widget()

        self.set_map_position(self._lat, self._lon, self._zoom)

        # add marker for Kumpulan kampus

        self.add_marker(KUMPULA_LAT, KUMPULA_LON, text="Kumpulan kampus")

    def set_handler(self, handler):
        """Set handler for signaling actions"""

        self._handler = handler

    def _init_map_widget(self) -> tkintermapview.TkinterMapView:
        container = self._container

        width = container.winfo_width()
        height = container.winfo_height()

        # initialize map widget

        map_widget = tkintermapview.TkinterMapView(
            container, width=width, height=height, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        return map_widget

    def reset_map_position(self):
        """Resets the map position and zoom level to default values"""

        self._lat = KUMPULA_LAT
        self._lon = KUMPULA_LON
        self._zoom = ZOOM_DEFAULT

        self._map.set_zoom(self._zoom)
        self._map.set_position(self._lat, self._lon)

    def zoom_out(self):
        """Zoom in map. Clamp at ZOOM_MIN."""

        new_zoom = self._zoom - 1

        if new_zoom < ZOOM_MIN:
            new_zoom = ZOOM_MIN

        self._zoom = new_zoom

        self._map.set_zoom(self._zoom)

    def zoom_in(self):
        """Zoom out map. Clamp at ZOOM_MAX."""

        new_zoom = self._zoom + 1

        if new_zoom > ZOOM_MAX:
            new_zoom = ZOOM_MAX

        self._zoom = new_zoom

        self._map.set_zoom(self._zoom)

    def set_map_position(self, lat, lon, zoom):
        """Sets the map position and zoom level"""

        self._lat = lat
        self._lon = lon
        self._zoom = zoom

        self._map.set_zoom(zoom)
        self._map.set_position(lat, lon)

    def add_marker(self, lat, lon, text=None):
        if text is None:
            self._log.error(
                "Can't add marker, lat: %s, lon: %s, text: %s", lat, lon, text)
            return

        marker = self._map.set_marker(lat, lon, text)

        marker_id = f"{text}_{lat}_{lon}"

        self._markers[marker_id] = marker

    def add_stop_marker(self, stop):
        if stop is None:
            self._log.error("Can't add marker, stop: %s", stop)
            return

        if str(stop.vehicle_type) == "3":
            icon_name = "harjoitustyo/res/image/icons8-bus-stop-100_edit.png"
        else:
            icon_name = "harjoitustyo/res/image/icons8-tram-100_edit.png"

        text = stop.stop_name
        lat = stop.lat
        lon = stop.lon

        image = PIL.Image.open(icon_name)
        resized = image.resize((50, 50))

        icon = PIL.ImageTk.PhotoImage(resized)

        def handler(data):
            data2 = stop
            self._handler.handle("map_marker_clicked", data, data2)

        marker = self._map.set_marker(
            lat, lon, text, icon=icon, command=handler)

        marker_id = f"{text}_{lat}_{lon}"

        self._markers[marker_id] = marker
