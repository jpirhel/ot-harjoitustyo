class StopContainer:
    """UI display element containing a single stop

    Updatable by calling the method update().
    """

    def __init__(self, container, log):
        """Initializes the stop, outer container and inner container.

        Also initializes the initial inner container.
        """

        self._log = log

        self._stop = None

        # outer container (tkinter Frame) for this element
        self._container = container

        # inner container (tkinter Frame) for this element
        self._inner_container = None

        # initialize inner container
        self._generate_inner_container()

    def set_stop(self, stop):
        """Sets the currently selected stop"""

        self._stop = stop

    def container(self):
        """Inner container."""

        return self._inner_container

    def update(self):
        """Updates the view, used top update displayed UI when a new stop is selected"""

        # NOTE: this is probably very inefficient

        # destroy the previous container
        self._inner_container.destroy()

        # generate the new container
        self._generate_inner_container()

        # display the new container - needed to actually update the display
        self._inner_container.pack()

    def _generate_inner_container(self):
        """Generates an inner container. Must be implemented by the inheriting classes.

        Raises:
            NotImplementedError (only this stub version)
        """

        raise NotImplementedError("Not implemented: StopContainer._generate_inner_container")
