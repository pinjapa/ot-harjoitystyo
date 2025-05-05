
class CountService:
    def __init__(self):
        self.points1 = 0
        self.points2 = 0
        self.card_values = {"6":0, "7":0, "8":0, "9":0, "J":2, "Q":3, "K":4, "10":10, "A":11}

    def count_cards(self, bag1, bag2):
        for card in bag1:
            self.points1 += self.card_values[card[0]]

        for card in bag2:
            self.points2 += self.card_values[card[0]]

        print(f"pisteitä yhteensä {self.points1+self.points2}")

    def last_trick(self, winner):
        if winner == 1:
            self.points1 += 20
        else:
            self.points2 += 20

    def total_game_points(self):
        pass
