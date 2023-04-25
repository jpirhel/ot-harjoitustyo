import logging

import tkinter as tk
import tkinter.ttk as ttk

from .map.map import Map
from .control.control import Control
from .handler.handler import Handler


class Ui:
    control_frame_width = 300  # pixels

    def __init__(self, container: tk.Frame):
        self._log = logging.getLogger("Ui")

        self._container = container

        width = container.winfo_width()
        height = container.winfo_height()

        # create info frame (left)

        control_frame_style = ttk.Style()
        control_frame_style.configure(
            "control_frame_style.TFrame", foreground="black", background="white")
        control_frame = ttk.Frame(
            master=container,
            width=self.control_frame_width,
            height=height,
            style="control_frame_style.TFrame")
        control_frame.grid(row=0, column=0)

        control_frame.update_idletasks()

        map_frame_width = width - self.control_frame_width
        # map_frame_width = 100

        # create map frame (right)

        map_frame_style = ttk.Style()
        map_frame_style.configure(
            "map_frame_style.TFrame", foreground="white", background="white")
        map_frame = ttk.Frame(
            container,
            width=map_frame_width,
            height=height,
            style="map_frame_style.TFrame")
        map_frame.grid(row=0, column=1)

        map_frame.update_idletasks()

        self._control = self._init_control(control_frame)
        self._map = self._init_map(map_frame)

        self._handler = self._init_handler()

        self._control.set_handler(self._handler)
        self._map.set_handler(self._handler)

    # noinspection PyMethodMayBeStatic
    def _init_map(self, container) -> Map:
        map_widget = Map(container)

        return map_widget

    # noinspection PyMethodMayBeStatic
    def _init_control(self, container):
        control_widget = Control(container)

        return control_widget

    def _init_handler(self):
        handler = Handler(self._control, self._map)
        return handler
