import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_tasmaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_osto_toimii_kateisella(self):
        edullinenHinta = 240
        riittava = 300
        riittamaton = 200


        # riittävät varat


        result = self.kassapaate.syo_edullisesti_kateisella(riittava)

        # käteistä vähennetty
        self.assertEqual(result, riittava - edullinenHinta)

        # kassaan lisätty rahaa
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + edullinenHinta)

        # myytyjen edullisten lounaiden määrä on oikea
        self.assertEqual(self.kassapaate.edulliset, 1)


        # riittämättömät varat


        result = self.kassapaate.syo_edullisesti_kateisella(riittamaton)

        # käteisestä ei vähennetty
        self.assertEqual(result, riittamaton)

        # kassaan ei lisätty rahaa
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + edullinenHinta)

        # myytyjen edullisten lounaiden määrä on edelleen oikea
        self.assertEqual(self.kassapaate.edulliset, 1)


    def test_maukkaan_lounaan_osto_toimii_kateisella(self):
        maukasHinta = 400
        riittava = 500
        riittamaton = 300


        # riittävät varat


        result = self.kassapaate.syo_maukkaasti_kateisella(riittava)

        # käteistä vähennetty
        self.assertEqual(result, riittava - maukasHinta)

        # kassaan lisätty rahaa
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + maukasHinta)

        # myytyjen maukkaiden lounaiden määrä on oikea
        self.assertEqual(self.kassapaate.maukkaat, 1)


        # riittämättömät varat


        result = self.kassapaate.syo_maukkaasti_kateisella(riittamaton)

        # käteisestä ei vähennetty
        self.assertEqual(result, riittamaton)

        # kassaan ei lisätty rahaa
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + maukasHinta)

        # myytyjen maukkaiden lounaiden määrä on edelleen oikea
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisen_lounaan_osto_toimii_kortilla(self):
        # riittävät varat kortilla


        maksukortti = Maksukortti(300)

        result = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        # maksutapahtuma onnistui
        self.assertEqual(result, True)

        # maksukorttia veloitettiin
        self.assertEqual(maksukortti.saldo, 300 - 240)
        # kassaan ei lisätty rahaa
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


        # riittämättömät varat kortilla


        maksukortti = Maksukortti(200)

        result = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        # maksutapahtuma epäonnistui
        self.assertEqual(result, False)

        # maksukorttia ei veloitettu
        self.assertEqual(maksukortti.saldo, 200)

        # kassaan ei lisätty rahaa
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_maukkaan_lounaan_osto_toimii_kortilla(self):
        # riittävät varat kortilla


        maksukortti = Maksukortti(500)

        result = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        # maksutapahtuma onnistui
        self.assertEqual(result, True)

        # maksukorttia veloitettiin
        self.assertEqual(maksukortti.saldo, 500 - 400)

        # kassaan ei lisätty rahaa
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


        # riittämättömät varat kortilla


        maksukortti = Maksukortti(300)

        result = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        # maksutapahtuma epäonnistui
        self.assertEqual(result, False)

        # maksukorttia ei veloitettu
        self.assertEqual(maksukortti.saldo, 300)

        # kassaan ei lisätty rahaa
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille(self):
        maksukortti = Maksukortti(0)

        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1)

        self.assertEqual(maksukortti.saldo, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 100)
