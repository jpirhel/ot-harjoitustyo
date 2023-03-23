import logging

import tkinter as tk
import tkinter.ttk as ttk

from .map.map import Map


class Ui:
    _info_frame_width = 300  # pixels

    def __init__(self, container: tk.Frame):
        self._log = logging.getLogger("Ui")

        self._container = container

        width = container.winfo_width()
        height = container.winfo_height()

        map_frame_width = width - self._info_frame_width

        # create map frame (left)

        map_frame_style = ttk.Style()
        map_frame_style.configure("map_frame_style.TFrame", foreground="white", background="white")
        map_frame = ttk.Frame(
            container,
            width=map_frame_width,
            height=height,
            style="map_frame_style.TFrame")
        map_frame.grid(row=0, column=0)

        map_frame.update_idletasks()

        # create info frame (right)

        info_frame_style = ttk.Style()
        info_frame_style.configure("info_frame_style.TFrame", foreground="black", background="white")
        info_frame = ttk.Frame(
            master=container,
            width=self._info_frame_width,
            height=height,
            style="info_frame_style.TFrame")
        # info_frame.lift()
        info_frame.grid(row=0, column=1)

        info_frame.update_idletasks()

        self._map = self._init_map(map_frame)

    # noinspection PyMethodMayBeStatic
    def _init_map(self, container) -> Map:
        map_widget = Map(container)

        return map_widget
