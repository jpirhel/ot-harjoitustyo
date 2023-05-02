# constants used in the app

# URL for the HSL static data zip file (https://www.hsl.fi/hsl/avoin-data)

DATA_URL = "https://infopalvelut.storage.hsldev.com/gtfs/hsl.zip"

DATA_FILE_NAME = "HSL.zip"

# set to true to skip actually downloading the data file

SKIP_FETCHING = False

# location of Kumpula kampus

KUMPULA_LAT = 60.204709920625845
KUMPULA_LON = 24.96215062546151

KUMPULA_COORD = (KUMPULA_LAT, KUMPULA_LON)

# default map settings

ZOOM_DEFAULT = 17
ZOOM_MAX = 19
ZOOM_MIN = 1

# prune the stop data to include stops under this distance

MAXIMUM_STOP_DISTANCE_FROM_CENTER = 1.0  # kilometers

SQLITE_FILE_NAME = "database.sqlite"

# tkinter button styling

BUTTON_DEFAULT_WIDTH = 8
BUTTON_DEFAULT_HEIGHT = 2

# tkinter font styling

FONT_BUTTON = ("Arial", 12)
FONT_TEXT = ("Arial", 14)
FONT_HEADER = ("Arial", 18)

# initial geometry for the app window

WINDOW_INITIAL_WIDTH = 1000
WINDOW_INITIAL_HEIGHT = 750
