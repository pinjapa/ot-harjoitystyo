import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(500)
    
    
    def test_kassapaate_luodaan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_edullinen_toimii_oikein(self):
        tapahtuma = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(tapahtuma, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_ei_kateista_edulliseen_toimii_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_maukas_toimii_oikein(self):
        tapahtuma = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
        self.assertEqual(tapahtuma, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_ei_kateista_maukkaaseen_toimii_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.maukkaat, 0) 

    def test_korttimaksu_edullinen_toimii_oikein(self):
        tapahtuma = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 2.6)
        self.assertEqual(tapahtuma, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_korttimaksu_maukas_toimii_oikein(self):
        tapahtuma = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 1)
        self.assertEqual(tapahtuma, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kortilla_ei_tarpeeksi_rahaa_edulliseen(self):
        kortti = Maksukortti(200)
        tapahtuma = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 2)
        self.assertEqual(tapahtuma, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)


    def test_kortilla_ei_tarpeeksi_rahaa_maukkaaseen(self):
        kortti = Maksukortti(200)
        tapahtuma = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 2)
        self.assertEqual(tapahtuma, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_rahan_talletus_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(self.kortti.saldo_euroina(), 7)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002)
    
    def test_yritetaan_tallettaa_negatiivinen_summa(self):
        tapahtuma = self.kassapaate.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kortti.saldo_euroina(), 5)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(tapahtuma, None)