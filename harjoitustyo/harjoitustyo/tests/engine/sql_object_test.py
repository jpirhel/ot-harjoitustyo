import unittest

from harjoitustyo.engine.route import Route


class TestSqlObject(unittest.TestCase):
    def setUp(self):
        # Route inherits from SQLObject

        route_data = """1001,HSL,1,Eira - Töölö - Sörnäinen (M) - Vallila,,0,http://aikataulut.hsl.fi/linjat/fi/h1_1a.html"""
        route = Route.from_string(route_data)
        self.route = route

    def test_as_list(self):
        lst = self.route.as_list()

        # self.assertIsInstance(lst, list)

        # self.assertEqual(len(lst), 7)

        correct = [
            '1001',
            'HSL',
            '1',
            'Eira - Töölö - Sörnäinen (M) - Vallila',
            '',
            '0',
            'http://aikataulut.hsl.fi/linjat/fi/h1_1a.html'
        ]

        self.assertEqual(lst, correct)