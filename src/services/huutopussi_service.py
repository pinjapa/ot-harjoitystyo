import random
#from services.count_service import CountService

class HuutopussiService:

    def __init__(self):
        self.pack = []
        self.hand1 = []
        self.hand2 = []
        self.bid_cards = []
        self._bid_win_hand = None
        self.played = []
        self.suits = self.suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
        self.bag1 = []
        self.bag2 = []
        self.trump = False
        self.rank_order = {"6":1, "7":2, "8":3, "9":4, "J":5, "Q":6, "K":7, "10":8, "A":9}

    def create_pack(self):
        ranks = ["6", "7", "8", "9", "J", "Q", "K", "10", "A"]
        for i in self.suits:
            for j in ranks:
                self.pack.append((j, i))

    def deal_cards(self):  # jakaa kortit
        random.shuffle(self.pack)
        self.hand1 = self.pack[:13]
        self.hand2 = self.pack[13:26]
        self.bid_cards = self.pack[32:36]
        #print(f"käsi 1 pituus {len(self.hand1)}")

    def bid_save(self, bid, bid_round):  # tallentaa korkeimman huudon
        if bid_round == 1:
            print(f"Tallennetaan huuto: {bid}")
        if bid_round == 2:
            print(f"Tallennetaan korotus: {bid}")

    def bid_win(self, hand, round): # lisää tarjouskierroksen voittajalle kortit
        if round == 2:
            if hand == "1":
                self._bid_win_hand = 1
                for card in self.bid_cards:
                    self.hand1.append(card)
                print(f"käsi 1 pituus {len(self.hand1)}")

            elif hand == "2":
                self._bid_win_hand = 2
                for card in self.bid_cards:
                    self.hand2.append(card)
            else:
                print("Virhe: Ilmoita pelaaja: 1 tai 2")

    def play_card(self, card, hand):
        if len(self.hand1) > 13:
            print(len(self.hand1))
            self.bag1.append(card)
            self.hand1.remove(card)
            return "Laita kortti pois ensin!"

        if len(self.hand2) > 13:
            self.bag2.append(card)
            self.hand2.remove(card)
            return "Laita kortti pois ensin!"

        if len(self.played) == 2:
            if self.trump:
                self.compare_trump(self.played[0], self.played[1])
            self.compare(self.played[0], self.played[1])
            self.played = []

        self.played.append((card, hand))

        return self.played

    def compare(self, card1, card2):  # ei valttia
        if card1[0][1] != card2[0][1]: #pelaajilla eri maata
            self.tricks(card1[1])
        else:
            self.compare_value(card1, card2)

    def compare_value(self, card1, card2):
        if self.rank_order[card1[0][0]] > self.rank_order[card2[0][0]]:
            self.tricks(card1[1])

        elif self.rank_order[card2[0][0]] > self.rank_order[card1[0][0]]:
            self.tricks(card2[1])
        else:
            print("Tänne ei pitäisi päästä")

    def compare_trump(self, card1, card2): # valtti olemassa
        if card1[0][1] != self.trump:
            if card2[0][1] != self.trump:
                self.compare(card1, card2)

        elif card1[0][1] == self.trump:
            if card2[0][1] != self.trump:
                self.tricks(card1[1])
            elif card2[0][1] == self.trump:
                self.compare_value(card1, card2)

    def tricks(self, win):
        if win == 1:
            self.bag1.append(self.played[0][0])
            self.bag1.append(self.played[1][0])
        if win == 2:
            self.bag2.append(self.played[0][0])
            self.bag2.append(self.played[1][0])
