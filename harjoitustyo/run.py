import argparse

from harjoitustyo.app import App
from harjoitustyo.engine.data.importer import Importer


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--import-data-from-web", action="store_true")
    args = parser.parse_args()

    import_data_from_web = args.import_data_from_web

    if import_data_from_web:
        importer = Importer()
        importer.import_data()
    else:
        app = App()
        app.run()


if __name__ == "__main__":
    main()
