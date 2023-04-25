import tkinter as tk

from harjoitustyo.constant import BUTTON_DEFAULT_WIDTH, BUTTON_DEFAULT_HEIGHT


class Control:
    def __init__(self, container):
        self._container = container
        self._handler = None

        inner_container = tk.Frame(master=container, width=200)

        self._inner_container = inner_container

        button_home_icon = tk.PhotoImage("harjoitustyo/res/image/icons8-home-100.png")
        print("button_home_icon: %s" % button_home_icon, flush=True)

        button_home = tk.Button(
            inner_container,
            width=BUTTON_DEFAULT_WIDTH,
            height=BUTTON_DEFAULT_HEIGHT,
            command=self._handle_home,
            )
        button_home.pack(side=tk.TOP)

        button_plus = tk.Button(
            inner_container,
            width=BUTTON_DEFAULT_WIDTH,
            height=BUTTON_DEFAULT_HEIGHT,
            command=self._handle_plus)
        button_plus.pack()

        button_minus = tk.Button(
            inner_container,
            width=BUTTON_DEFAULT_WIDTH,
            height=BUTTON_DEFAULT_HEIGHT,
            command=self._handle_minus)
        button_minus.pack()

        inner_container.grid(row=0, column=0)

    def set_handler(self, handler):
        """Set handler for signaling actions"""

        self._handler = handler

    def _handle_home(self):
        self._handler.handle("map_home")

    def _handle_plus(self):
        self._handler.handle("map_plus")

    def _handle_minus(self):
        self._handler.handle("map_minus")

    def stop_info(self, stop):
        print(f"Control.stop_info, stop: {stop}", flush=True)
