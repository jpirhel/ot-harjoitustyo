import tkinter as tk

from harjoitustyo.constant import BUTTON_DEFAULT_WIDTH, BUTTON_DEFAULT_HEIGHT, FONT_BUTTON


class MapButtons:
    """Buttons for controlling the map"""

    def __init__(self, container):
        """Initializes the instance of MapButtons.

        Args: tkinter frame containing the buttons
        """

        self._handler = None

        container_width = container.winfo_width()
        button_container = tk.Frame(master=container, width=container_width)

        button_home = tk.Button(
            button_container,
            font=FONT_BUTTON,
            text="koti",
            width=BUTTON_DEFAULT_WIDTH,
            height=BUTTON_DEFAULT_HEIGHT,
            command=self._handle_home,
        )

        button_home.grid(row=0, column=0)

        button_plus = tk.Button(
            button_container,
            text="lähennä",
            font=FONT_BUTTON,
            width=BUTTON_DEFAULT_WIDTH,
            height=BUTTON_DEFAULT_HEIGHT,
            command=self._handle_plus)

        button_plus.grid(row=0, column=1, padx=10)

        button_minus = tk.Button(
            button_container,
            text="loitonna",
            font=FONT_BUTTON,
            width=BUTTON_DEFAULT_WIDTH,
            height=BUTTON_DEFAULT_HEIGHT,
            command=self._handle_minus)

        button_minus.grid(row=0, column=2)

        self._button_container = button_container

    def container(self):
        """Container containing the buttons."""

        return self._button_container

    def set_handler(self, handler):
        """Sets the handler for UI actions."""

        self._handler = handler

    def _handle_home(self):
        """Navigate to map home.

        Map home is the default location and zoom for the map.
        """

        self._handler.handle("map_home")

    def _handle_plus(self):
        """Zoom in map."""

        self._handler.handle("map_plus")

    def _handle_minus(self):
        """Zoom out map."""

        self._handler.handle("map_minus")
