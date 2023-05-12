import math
import logging
import datetime

from functools import cmp_to_key

import tkinter as tk

from harjoitustyo.constant import FONT_HEADER, FONT_TEXT, FONT_INFO

from .stop_container import StopContainer


class StopTimesInfo(StopContainer):
    """Displays stop time info for a stop"""

    def __init__(self, container):
        """Initializes the class with an empty private variable for stop times"""

        self._log = logging.getLogger("StopTimesInfo")

        super().__init__(container, self._log)

        self._stop_times = None

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

        now = datetime.datetime.now()

        # container for all stop times

        stc = tk.Frame(inner_container, pady=10)
        stc.pack()

        lw = 8  # label width

        # hack to deduplicate stop times

        # weekdays: 0: mon-fri, 5: saturday, 6: sunday

        now_weekday = now.weekday()

        if now_weekday < 5:
            now_weekday = 0

        stop_times = dict()

        for stop_time in self._stop_times:
            # check if stop time is not on this weekday
            # note that mon-fri is treated equally

            if now_weekday != stop_time.weekday():
                continue

            key = f"{stop_time.hour()}_{stop_time.minute()}__{stop_time.route_short_name}"
            stop_times[key] = stop_time

        st = list(stop_times.values())

        def comp(a, b):
            # compare hours

            if a.hour() > b.hour():
                return 1

            if b.hour() > a.hour():
                return -1

            # identical hours, compare minutes

            if a.minute() > b.minute():
                return 1

            if b.minute() > a.minute():
                return -1

            # identical hours and minutes

            return 0

        # sort stop times by arrival time

        st = sorted(st, key=cmp_to_key(comp))

        displayed_count = 0

        # header for displaying column help text

        header_container = tk.Frame(stc)
        header_container.pack()

        header_1 = tk.Label(header_container, text="kulkun.", width=lw, anchor="w")
        header_1.grid(row=0, column=1)

        header_2 = tk.Label(header_container, text="kello", width=lw, anchor="w")
        header_2.grid(row=0, column=2)

        header_3 = tk.Label(header_container, text="minuuttia", width=lw, anchor="w")
        header_3.grid(row=0, column=3)

        for stop_time in st:
            hour = stop_time.hour()
            minute = stop_time.minute()

            # check that the arrival is in the future

            if now.hour > hour:
                continue

            if now.hour == hour and  now.minute > minute:
                continue

            displayed_count += 1

            # use math.floor()
            # if a bus arrives in say 5min 30 seconds,
            # it is better to display it as 5 rather than 6 minutes

            minutes_to_arrival = math.floor(((hour - now.hour) * 60) + (minute - now.minute))

            arrival_display = stop_time.display_time()

            # container for this stop time

            c = tk.Frame(stc)
            c.pack()

            # color code arrival times by urgency

            if minutes_to_arrival <= 1:
                bg = "red"
            elif minutes_to_arrival <= 5:
                bg = "lightgreen"
            elif minutes_to_arrival <= 10:
                bg = "yellow"
            else:
                bg = "white"

            # label for bus / tram number

            lb = tk.Label(c, text=stop_time.route_short_name, font=FONT_INFO, width=lw, anchor="w", bg="white")
            lb.grid(row=0, column=0)

            # label for arrival time

            la = tk.Label(c,
                          text=arrival_display,
                          font=FONT_INFO,
                          width=lw,
                          anchor="w",
                          bg=bg)
            la.grid(row=0, column=1)

            if minutes_to_arrival > 60:
                hours = math.floor(minutes_to_arrival / 60)
                minutes = math.floor(minutes_to_arrival % 60)
                arrival_minutes_display_text = f"{hours}h {minutes}m"
            else:
                arrival_minutes_display_text = minutes_to_arrival

            # label for arrival time in minutes
            lm = tk.Label(c,
                          text=arrival_minutes_display_text,
                          font=FONT_INFO,
                          width=lw,
                          anchor="w",
                          bg=bg)
            lm.grid(row=0, column=2)

        # if no stop times are displayed, show a label telling that there are no more arrivals

        if displayed_count == 0:
            lb = tk.Label(stc, text="ei enää vuoroja tänään", font=FONT_TEXT)
            lb.pack()
