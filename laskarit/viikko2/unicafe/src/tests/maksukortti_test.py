import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_alussa_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
    
    def test_rahan_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 15)
    
    def test_saldo_vahenee_oikein_rahaa_rapeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5)

    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_palautta_true_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(900), True)

    def test_palauttaa_false_jos_rahat_eivat_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
