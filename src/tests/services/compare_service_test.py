import unittest
from services.compare_service import CompareService

class TestCompareService(unittest.TestCase):
    def setUp(self):
        self.service = CompareService()

    def test_start_compare(self):
        self.service.trump = "\u2663"
        self.service.hand1 = [("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663")]
        self.service.hand2 = [("K", "\u2665"), ("Q", "\u2665"), ("J", "\u2665")]
        self.service.played = [(("K", "\u2665"), 2), (("K", "\u2663"), 1)]
        self.service.start_compare()
        self.assertEqual(len(self.service.bag1), 2)

        self.service.trump = False
        self.service.played = [(("Q", "\u2663"), 1), (("Q", "\u2665"), 2)]
        self.service.start_compare()
        self.assertEqual(len(self.service.bag1), 4)

    def test_comapare_suits(self):
        self.service.played = [(("K", "\u2663"), 1), (("K", "\u2665"), 2)]
        self.service.compare_suits(self.service.played[0], self.service.played[1])
        self.assertEqual(self.service.bag1, [("K", "\u2663"), ("K", "\u2665")])

        self.service.played = [(("K", "\u2663"), 2), (("K", "\u2665"), 1)]
        self.service.compare_suits(self.service.played[0], self.service.played[1])
        self.assertEqual(self.service.bag2, [("K", "\u2663"), ("K", "\u2665")])

    def test_compare_value(self):
        self.service.played = [(("K", "\u2665"), 1), (("7", "\u2665"), 2)]
        self.service.compare_suits(self.service.played[0], self.service.played[1])
        self.assertEqual(self.service.bag1, [("K", "\u2665"), ("7", "\u2665")])
            
        self.service.played = [(("7", "\u2663"), 2), (("K", "\u2663"), 1)]
        self.service.compare_suits(self.service.played[0], self.service.played[1])
        self.assertEqual(self.service.bag1, [("K", "\u2665"), ("7", "\u2665"), ("7", "\u2663"), ("K", "\u2663")])

    def test_tricks(self):
        self.service.bag1 = [("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663")]
        self.service.played = [(("K", "\u2663"), 1), (("K", "\u2665"), 2)]
        
        self.assertEqual(self.service.tricks(1), (True, 1))
        self.service.bag1 = [("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663"), ("Q", "\u2663"), ("J", "\u2663"),
                            ("K", "\u2663")]
        self.service.played = [(("K", "\u2663"), 1), (("K", "\u2665"), 2)]
        self.assertEqual(self.service.tricks(2), (True, 2))

        self.assertEqual(self.service.tricks(3), (False, None))
