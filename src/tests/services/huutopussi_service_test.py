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
        self.assertEqual(len(self.game.bid_cards), 4)
        self.assertEqual(len(set(self.game.pack)), len(self.game.pack))
    
    def test_bid_win(self):

        self.game.bid_win("1", 2)
        self.assertEqual(len(self.game.hand1), 17)

        self.game.bid_win("2", 2)
        self.assertEqual(len(self.game.hand2), 17)
    
    def test_play_card_hand1(self):
        self.game.bid_win("1", 2)
        self.game.play_card(self.game.hand1[0], "1")

        self.assertEqual(len(self.game.hand1), 16)
        self.assertEqual(len(self.game.bag1), 1)
        self.assertEqual(len(self.game.bag2), 0)

    def test_play_card_hand2(self):
        self.game.bid_win("2", 2)
        self.game.play_card(self.game.hand2[0], "2")

        self.assertEqual(len(self.game.hand2), 16)
        self.assertEqual(len(self.game.bag2), 1)
        self.assertEqual(len(self.game.bag1), 0)

    def test_comapare_suits(self):
        self.game.played = [(("K", "\u2663"), 1), (("K", "\u2665"), 2)]
        self.game.compare_suits(self.game.played[0], self.game.played[1])
        self.assertEqual(self.game.bag1, [("K", "\u2663"), ("K", "\u2665")])

        self.game.played = [(("K", "\u2663"), 2), (("K", "\u2665"), 1)]
        self.game.compare_suits(self.game.played[0], self.game.played[1])
        self.assertEqual(self.game.bag2, [("K", "\u2663"), ("K", "\u2665")])
    
    def test_compare_value(self):
        self.game.played = [(("K", "\u2665"), 1), (("7", "\u2665"), 2)]
        self.game.compare_suits(self.game.played[0], self.game.played[1])
        self.assertEqual(self.game.bag1, [("K", "\u2665"), ("7", "\u2665")])
        
        self.game.played = [(("7", "\u2663"), 2), (("K", "\u2663"), 1)]
        self.game.compare_suits(self.game.played[0], self.game.played[1])
        self.assertEqual(self.game.bag1, [("K", "\u2665"), ("7", "\u2665"), ("7", "\u2663"), ("K", "\u2663")])