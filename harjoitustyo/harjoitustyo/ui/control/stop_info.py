import webbrowser
import tkinter as tk

from harjoitustyo.constant import FONT_HEADER, FONT_TEXT


class StopInfo:
    """Displays information about public transport stops"""

    def __init__(self, container):
        self._stop = None

        self._container = container

        self._generate_inner_container()

    def _generate_inner_container(self):
        """Generates a inner container including all the stop related info"""

        inner_container = tk.Frame(self._container)

        label = tk.Label(inner_container, text="pysäkin tiedot", font=FONT_HEADER)
        label.pack()

        self._inner_container = inner_container

        stop_info = self._stop_info()
        stop_info.pack()

        inner_container.pack(pady=10)

    def container(self):
        return self._inner_container

    def update(self):
        """Updates the stop view, used top update displayed UI when a new stop is selected"""

        # NOTE this is probably very inefficient

        # destroy previous container

        self._inner_container.destroy()

        # generate new container

        self._generate_inner_container()

    def set_stop(self, stop):
        """Sets the currently selected stop"""

        self._stop = stop

    def _stop_info(self):
        """Displays stop info for a selected stop or help text when no stop is selected"""

        container = tk.Frame(self._inner_container, highlightthickness="2", highlightcolor="red")

        stop = self._stop

        if stop is None:
            name_frame = tk.Frame(container, pady=10)
            name_frame.grid()

            # help text when no stop is selected

            name = tk.Label(name_frame, text="valitse pysäkki kartalta", font=FONT_TEXT)
            name.pack()
        else:
            code_frame = tk.Frame(container, pady=10)
            code_frame.grid(row=0, column=0)

            code = tk.Label(code_frame, text=stop.stop_code, font=FONT_TEXT)
            code.pack()

            # stop name

            name = tk.Label(container, text=stop.stop_name, font=FONT_TEXT)
            name.grid(row=1, column=0)

            # stop description, usually containing approximate stop address

            desc = tk.Label(container, text=stop.stop_desc, font=FONT_TEXT)
            desc.grid(row=2, column=0)

            url_frame = tk.Frame(container, pady=10)
            url_frame.grid(row=3, column=0)

            # a clickable link to HSL.fi website containing the stop timetable

            url = tk.Label(url_frame, text="aikataulut (hsl.fi)", font=FONT_TEXT, fg="blue", cursor="hand2")
            url.pack()

            # when button is clicked, open a new browser tab to HSL.fi

            url.bind("<Button-1>", lambda e: webbrowser.open_new_tab(stop.corrected_stop_url()))

        return container
