import logging

import tkinter as tk

from harjoitustyo.constant import FONT_HEADER

from .stop_container import StopContainer


class StopTimesInfo(StopContainer):
    """Displays stop time info for a stop"""

    def __init__(self, container):
        """Initializes the class with an empty private variable for stop times"""

        super().__init__(container)

        self._stop_times = None

        self._log = logging.getLogger("StopTimesInfo")

    def set_stop_times(self, stop_times):
        """Sets the stop times"""

        self._stop_times = stop_times

    def _generate_inner_container(self):
        """Generates an inner container including all the stop time related info"""

        inner_container = tk.Frame(self._container)
        self._inner_container = inner_container

        # empty element if no stop is selected

        if self._stop is None:
            self._log.error("Can't generate inner container, empty stop")
            return

        # empty element if stop times are not available

        if self._stop_times is None:
            self._log.error("Can't generate inner container, empty stop times")
            return

        label = tk.Label(inner_container, text="aikataulut", font=FONT_HEADER)
        label.pack()

        for i in range(5):
            l = tk.Label(inner_container, text=str(i), font=FONT_HEADER)
            l.pack()
