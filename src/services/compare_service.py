
class CompareService:
    """Luokka, joka vastaa korttien vertailusta"""

    def __init__(self):
        self.hand1 = []
        self.hand2 = []
        self.played = None
        self.trump = False
        self.bag1 = []
        self.bag2 = []
        self.rank_order = {"6":1, "7":2, "8":3, "9":4, "J":5, "Q":6, "K":7, "10":8, "A":9}
        self.turn = 1


    def start_compare(self):
        card1 = self.played[0]
        card2 = self.played[1]
        if self.trump:
            end = self.compare_trump(card1, card2)
        else:
            end = self.compare_suits(card1, card2)
        result = (card1, card2)

        if self.played[0][1] == 1:
            self.hand1.remove(self.played[0][0])
            self.hand2.remove(self.played[1][0])
        else:
            self.hand2.remove(self.played[0][0])
            self.hand1.remove(self.played[1][0])

        if end[0] is True:
            return (end[0], end[1])

        return result

    def compare_suits(self, card1, card2):
        """Vertailee, ovatko kortit samaa maata.

        Args:
            card1: Kahdesta kortista ensin pelattu, ja kumpi pelaaja
            card2: Toiseksi pelattu kortti, ja sen pelaaja
        """
        if card1[0][1] != card2[0][1]:
            return self.tricks(card1[1])

        return self.compare_value(card1, card2)

    def compare_trump(self, card1, card2):
        """ Vertailee kortteja, kun valtti on olemassa.

        Args:
            card1: Kahdesta kortista ensin pelattu, ja kumpi pelaaja
            card2: Toiseksi pelattu kortti, ja sen pelaaja
        """
        if self.trump not in (card1[0][1], card2[0][1]):
            return self.compare_suits(card1, card2)

        if card1[0][1] == self.trump:
            return self.compare_suits(card1, card2)

        if card2[0][1] == self.trump:
            return self.tricks(card2[1])

        return self.compare_value(card1, card2)

    def compare_value(self, card1, card2):
        """ Vertailee, kumpi korteista on suurempi.

        Args:
            card1: Kahdesta kortista ensin pelattu, ja sen pelaaja
            card2: Toiseksi pelattu kortti, ja sen pelaaja
        """
        if self.rank_order[card1[0][0]] > self.rank_order[card2[0][0]]:
            return self.tricks(card1[1])

        return self.tricks(card2[1])

    def tricks(self, win):
        """ Kumman pelaajan kortti on suurempi, sen "pussiin" lisätään kääntö.

        Args:
            win: Kumman pelaajan kortti on suurempi.
        """

        if win == 1:
            self.bag1.append(self.played[0][0])
            self.bag1.append(self.played[1][0])
            self.turn = 1
            if len(self.bag1)+len(self.bag2) == 30:

                return (True, win)
            return (False, None)

        if win == 2:
            self.bag2.append(self.played[0][0])
            self.bag2.append(self.played[1][0])
            self.turn = 2
            if len(self.bag1)+len(self.bag2) == 30:

                return (True, win)
            return (False, None)

        return (False, None)
