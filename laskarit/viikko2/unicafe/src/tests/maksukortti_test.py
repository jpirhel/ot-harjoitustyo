import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodun_kortin_alkusaldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_rahan_ottaminen_toimii(self):
        result = self.maksukortti.ota_rahaa(600)

        # rahan ottaminen toimi
        self.assertEqual(result, True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 4.00 euroa")

        result = self.maksukortti.ota_rahaa(600)

        # rahan ottaminen ei toiminut
        self.assertEqual(result, False)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 4.00 euroa")
