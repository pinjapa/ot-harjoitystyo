import unittest
from services.count_service import CountService

class TestCountService(unittest.TestCase):
    def setUp(self):
        self.service = CountService()
    
    def test_created_correctly(self):
        self.assertEqual(self.service.points1, 0)
        self.assertEqual(self.service.points2, 0)
    
    def test_count_cards(self):
        bag1 = [("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("9", "\u2663"), ("8", "\u2663"), ("7", "\u2663"),
                            ("6", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663")]
        bag2 = [("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"), #4p vähemmän
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("6", "\u2663")]
        self.service.count_cards(bag1, bag2)
        self.assertEqual(self.service.points1, 40+27+18)
        self.assertEqual(self.service.points2, 36+27+18)

    def test_last_trick(self):
        self.service.last_trick(1)
        self.assertEqual(self.service.points1, 20)

        self.service.last_trick(2)
        self.assertEqual(self.service.points2, 20)

    def test_trump_done(self):
        self.service.trump_done("\u2660", 2)
        self.assertEqual(self.service.points2, 40)

        self.service.trump_done("\u2666", 2)
        self.assertEqual(self.service.points2, 120)

        self.service.trump_done("\u2665", 1)
        self.assertEqual(self.service.points1, 100)

        self.service.trump_done("\u2663", 1)
        self.assertEqual(self.service.points1, 160)

    def test_no_bid_player(self):
        self.service.points1 = 31
        self.service.no_bid_player(1)
        
        self.assertEqual(self.service.game_points1, 31)

        self.service.points2 = 56
        self.service.no_bid_player(2)
        
        self.assertEqual(self.service.game_points2, 56)