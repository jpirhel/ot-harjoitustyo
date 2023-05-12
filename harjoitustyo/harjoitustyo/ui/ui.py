import logging

import tkinter as tk
import tkinter.ttk as ttk

from .map.map import Map
from .control.control import Control
from .handler.handler import Handler
from ..constant import UI_CONTROL_FRAME_WIDTH


class Ui:
    """The visible UI of the application.

    Contains the control frame on the left and the map frame on the right.
    """

    control_frame_width = UI_CONTROL_FRAME_WIDTH

    def __init__(self, container: tk.Frame):
        """Initializes the instance based on the tkinter container frame.

        Args:
            container: The container containing the initialized UI
        """

        self._log = logging.getLogger("Ui")

        self._container = container

        width = container.winfo_width()
        height = container.winfo_height()

        # create control frame (left)

        control_frame_style = ttk.Style()

        control_frame_style.configure(
            "control_frame_style.TFrame",
            foreground="black",
            background="white",
        )

        control_frame = ttk.Frame(
            master=container,
            width=self.control_frame_width,
            height=height,
            style="control_frame_style.TFrame")

        control_frame.place(x=0, y=0)

        control_frame.update_idletasks()

        map_frame_width = width - self.control_frame_width

        # create map frame (right)

        map_frame_style = ttk.Style()

        map_frame_style.configure(
            "map_frame_style.TFrame", foreground="white", background="white")

        map_frame = ttk.Frame(
            container,
            width=map_frame_width,
            height=height,
            style="map_frame_style.TFrame")

        map_frame.place(x=self.control_frame_width, y=0)

        map_frame.update_idletasks()

        self._control = self._init_control(control_frame)
        self._map = self._init_map(map_frame)

        self._handler = self._init_handler()

        self._control.set_handler(self._handler)
        self._map.set_handler(self._handler)

    # noinspection PyMethodMayBeStatic
    def _init_map(self, container) -> Map:
        """Initializes the Map widget.

        Returns:
            Instance of the Map widget
        """

        map_widget = Map(container)

        return map_widget

    # noinspection PyMethodMayBeStatic
    def _init_control(self, container):
        """Initializes the Control widget.

        Returns:
            Instance of the Control widget
        """

        control_widget = Control(container)

        return control_widget

    def _init_handler(self):
        """Initializes the Handler widget.

        The Handler widget contains callback functions for handling UI events,
        for example button clicks.

        Returns:
            Instance of the Handler widget
        """
        handler = Handler(self._control, self._map)
        return handler
