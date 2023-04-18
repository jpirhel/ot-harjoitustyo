class SQLObject:
    def as_list(self):
        ret = []

        items = vars(self).items()

        for item in items:
            value = item[1] or ""
            ret.append(value)

        return ret

    @staticmethod
    def clean_string(data_string: str):
        parts = data_string.split(",")

        cleaned = []

        for part in parts:
            cleaned.append(part.strip().replace('"', ''))

        return cleaned
