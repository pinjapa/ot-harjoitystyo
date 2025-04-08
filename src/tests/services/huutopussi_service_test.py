import unittest
from services.huutopussi_service import HuutopussiService

class TestHuutopussiService(unittest.TestCase):
    def setUp(self):
        self.game = HuutopussiService()
        self.game.create_pack()
        self.game.deal_cards()

    def test_create_pack_works(self):

        self.assertEqual(len(self.game.pack), 36)

    def test_dealing_cards_works(self):

        self.assertEqual(len(self.game.hand1), 13)
        self.assertEqual(len(self.game.hand2), 13)
        self.assertEqual(len(self.game.out_of_game), 6)
        self.assertEqual(len(self.game.bid_cards), 4)
        self.assertEqual(len(set(self.game.pack)), len(self.game.pack))
