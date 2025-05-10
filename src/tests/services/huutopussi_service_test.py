import unittest
from services.huutopussi_service import HuutopussiService
from initialize_database import initialize_database

class TestHuutopussiService(unittest.TestCase):
    def setUp(self):
        self.game = HuutopussiService()
        self.game.create_pack()
        initialize_database()

    def test_create_game(self):

        self.assertEqual(len(self.game.suits), 4)

    def test_dealing_cards_works(self):

        self.assertEqual(len(self.game.hand1), 13)
        self.assertEqual(len(self.game.hand2), 13)
        self.assertEqual(len(self.game.bid_cards), 4)
        self.assertEqual(self.game.hand1, self.game.compare.hand1)
    
    def test_bid_save(self):
        self.game.bid_save(50, 2)
        self.assertEqual(self.game.bid, 50)

        self.game.bid_save(50, 3)
        self.assertEqual(self.game.bid2, 50)
        self.assertEqual(self.game.id, 1)

    def test_bid_win(self):

        self.game.bid_win("1", 1)
        self.assertEqual(self.game.compare.turn, 1)
        self.assertEqual(len(self.game.hand1), 17)

        self.game.bid_win("2", 1)
        self.assertEqual(self.game.compare.turn, 2)
        self.assertEqual(len(self.game.hand2), 17)

        
        self.assertEqual(self.game.bid_win("3", 2), False)
    
    def test_play_card_hand1(self):
        self.game.bid_win("1", 1)
        self.game.play_card(self.game.hand1[0], "1")

        self.assertEqual(len(self.game.hand1), 16)
        self.assertEqual(len(self.game.compare.bag1), 1)
        self.assertEqual(len(self.game.compare.bag2), 0)

    def test_play_card_hand2(self):
        self.game.bid_win("2", 1)
        self.game.play_card(self.game.hand2[0], "2")

        self.assertEqual(len(self.game.hand2), 16)
        self.assertEqual(len(self.game.compare.bag2), 1)
        self.assertEqual(len(self.game.compare.bag1), 0)

    def test_check_rules(self):
        self.game.hand1 = [("6", "\u2663"), ("6", "\u2665")]
        self.game.hand2 = [("6", "\u2663"), ("6", "\u2665")]
        self.game.played = [(("7", "\u2663"), 2)]
        
        self.assertEqual(self.game.check_rules(("6", "\u2665"), 1), False)

        self.assertEqual(self.game.check_rules(("6", "\u2663"), 1), True)

        self.game.played = [(("7", "\u2663"), 1)]

        self.assertEqual(self.game.check_rules(("6", "\u2665"), 2), False)

        self.assertEqual(self.game.check_rules(("6", "\u2663"), 2), True)


