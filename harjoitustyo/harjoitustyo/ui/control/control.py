import tkinter as tk

from .map_buttons import MapButtons
from .stop_info import StopInfo


class Control:
    """Controls UI.

    Contains elements for controlling the map and displaying Stop info.
    """

    _inner_container_width = 200
    _selected_stop = None

    def __init__(self, container):
        """Initializes an instance of the Control class.

        Args:
            container: tkinter container for containing the Control UI.
        """

        self._container = container
        self._handler = None

        # create Tk frame for containing control elements

        inner_container = tk.Frame(master=container, width=self._inner_container_width)
        inner_container.grid(padx=10, pady=10)

        self._inner_container = inner_container

        # create container for buttons controlling map

        buttons = MapButtons(inner_container)
        buttons.container().pack()

        self._buttons = buttons

        # create container for showing stop info

        stop_info = StopInfo(inner_container)
        stop_info.container().pack()

        self._stop_info = stop_info

    def set_handler(self, handler):
        """Sets handler for signaling actions."""

        self._handler = handler

        # set handle for child elements

        self._buttons.set_handler(handler)

    def stop_info(self, stop):
        """Displays information for a single Stop."""

        print(f"Control.stop_info, stop: {stop}", flush=True)

        self._selected_stop = stop

        self._stop_info.set_stop(stop)
        self._stop_info.update()

    def clear_stop(self):
        """Clears the currently selected Stop."""

        self._selected_stop = None
