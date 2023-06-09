import logging
import platform

import tkinter as tk
from tkinter import ttk

from .constant import WINDOW_INITIAL_WIDTH, WINDOW_INITIAL_HEIGHT
from .ui.ui import Ui


class App:
    """Main application for course project (harjoitustyo)."""

    def __init__(self):
        self._log = logging.getLogger("App")

        # tkinter root window

        self._root = self._init_root_window()

        # "main" container for app - contains all UI elements

        self._container = self._init_ui_container()

        self._ui = self._init_ui()

    def _init_root_window(self) -> tk.Tk:
        """Initializes the root tkinter window of the application."""

        root = tk.Tk()

        width_initial = WINDOW_INITIAL_WIDTH
        height_initial = WINDOW_INITIAL_HEIGHT

        # initial geometry size for restoring window from maximized state
        root.geometry(f"{width_initial}x{height_initial}")

        # root.bind("<Escape>", self._handle_escape)

        # maximize window at app startup
        # maximizing the app window works differently on Windows and Linux

        try:
            if platform.system() == "Windows":
                root.state("zoomed")
            else:
                root.attributes('-zoomed', True)
        except tk.TclError:
            self._log.warning("Failed to maximize window")

        # update idletasks to refresh geometry info (winfo_*())
        root.update_idletasks()

        root.title("Harjoitustyö")

        root_geometry = root.winfo_geometry()

        self._log.info("root_geometry: %s", root_geometry)

        return root

    def _init_ui_container(self) -> ttk.Frame:
        """Initializes the tkinter container for app UI.

        Returns:
             tkinter frame containing the UI
        """

        width = self._root.winfo_width()
        height = self._root.winfo_height()

        container = ttk.Frame(self._root, width=width, height=height)

        # Add container to root window
        container.pack()

        container.update_idletasks()

        return container

    def _init_ui(self) -> Ui:
        """Initializes the UI.

        Returns:
             Instance of the UI class representing the UI
        """

        return Ui(self._container)

    def _handle_escape(self):
        """Handler for escape key - exists app."""

        self._root.destroy()

    def run(self):
        """Starts root window main tkinter loop."""

        self._root.mainloop()
