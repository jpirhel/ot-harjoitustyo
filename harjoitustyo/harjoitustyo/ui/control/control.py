import tkinter as tk

from .map_buttons import MapButtons

from .stop_info import StopInfo
from .stop_times_info import StopTimesInfo

from ...constant import SQLITE_FILE_NAME, UI_LEFT_FRAME_WIDTH
from ...engine.data.reader import Reader


class Control:
    """Controls UI.

    Contains elements for controlling the map and displaying Stop info.
    """

    _inner_container_width = UI_LEFT_FRAME_WIDTH
    _selected_stop = None

    def __init__(self, container):
        """Initializes an instance of the Control class.

        Args:
            container: tkinter container for containing the Control UI.
        """

        self._container = container
        self._handler = None

        self._reader = Reader(SQLITE_FILE_NAME)
        # create Tk frame for containing control elements

        inner_container = tk.Frame(
            master=container,
            width=self._inner_container_width)

        inner_container.grid(padx=10, pady=10)

        self._inner_container = inner_container

        # create container for buttons controlling map

        buttons_container = tk.Frame(
            master=inner_container,
            width=self._inner_container_width)

        buttons_container.grid(row=0, column=0)

        buttons = MapButtons(buttons_container)
        buttons.container().pack()
        self._buttons = buttons

        # create container for showing stop info

        stop_info_container = tk.Frame(
            master=inner_container,
            width=self._inner_container_width,
        )

        stop_info_container.grid(row=1, column=0)

        stop_info = StopInfo(stop_info_container)
        stop_info.container().pack()

        self._stop_info = stop_info

        stop_times_info_container = tk.Frame(
            master=inner_container,
            width=self._inner_container_width)

        stop_times_info_container.grid(row=2, column=0)

        stop_times_info = StopTimesInfo(stop_times_info_container)
        stop_times_info.container().pack()

        self._stop_times_info = stop_times_info

    def set_handler(self, handler):
        """Sets handler for signaling actions."""

        self._handler = handler

        # set handle for child elements

        self._buttons.set_handler(handler)

    def stop_info_with_timetable(self, stop):
        """Displays information for a single Stop, including the timetable."""

        self._selected_stop = stop

        # update general info displayed about a stop

        self._stop_info.set_stop(stop)

        self._stop_info.update()

        # update the stop timetable when the selected stop changes

        stop_times = self._reader.read_stop_times(stop)

        self._stop_times_info.set_stop(stop)
        self._stop_times_info.set_stop_times(stop_times)

        self._stop_times_info.update()

    def clear_stop(self):
        """Clears the currently selected Stop."""

        self._selected_stop = None
