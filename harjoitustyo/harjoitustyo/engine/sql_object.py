class SQLObject:
    """Common functionality of all the SQL-based data types."""

    def as_list(self):
        """Converts the class instance attributes into a list.

        Used when inserting data into SQLite.

        Returns:
             list of tuples of instance attributes and their values.
        """

        ret = []

        items = vars(self).items()

        for item in items:
            value = item[1] or ""
            ret.append(value)

        return ret

    @staticmethod
    def clean_string(data_string: str):
        """Cleans the data string values.

        Returns:
             List of cleaned data parts.
        """

        parts = data_string.split(",")

        cleaned = []

        for part in parts:
            cleaned.append(part.strip().replace('"', ''))

        return cleaned
