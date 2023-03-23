import logging

import tkinter as tk

import tkintermapview


class Map:
    def __init__(self, container):
        self._container = container

        self._log = logging.getLogger("App.Ui.Map")

        self._markers = dict()

        # Kumpulan kampus coordinates
        self._lat = 60.204709920625845
        self._lon = 24.96215062546151

        # initial zoom level
        self._zoom = 17

        self._map = self._init_map_widget()

        self._init_map_position()

        self._add_initial_marker()

    def _init_map_widget(self) -> tkintermapview.TkinterMapView:
        container = self._container

        width = container.winfo_width()
        height = container.winfo_height()

        # initialize map widget

        map_widget = tkintermapview.TkinterMapView(container, width=width, height=height, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        return map_widget

    def _init_map_position(self):
        self._map.set_position(self._lat, self._lon)
        self._map.set_zoom(self._zoom)

    def _add_initial_marker(self):
        m1 = self._map.set_position(self._lat, self._lon, marker=True)
        m1.set_text("Kumpulan kampus")

        self._markers["kumpulan_kampus"] =  m1
