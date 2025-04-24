import random

class HuutopussiService:

    def __init__(self):
        self.hand1 = []
        self.hand2 = []
        self.bid_cards = []
        self.played = []
        self.bag1 = []
        self.bag2 = []

    def create_pack(self):
        self.pack = []
        ranks = ["6", "7", "8", "9", "J", "Q", "K", "10", "A"]
        self.suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
        for i in self.suits:
            for j in ranks:
                self.pack.append((j, i))

    def deal_cards(self):  # jakaa kortit
        random.shuffle(self.pack)
        self.hand1 = self.pack[:13]
        self.hand2 = self.pack[13:26]
        self.out_of_game = self.pack[26:32]
        self.bid_cards = self.pack[32:36]

    def bid_save(self, bid, bid_round):  # tallentaa korkeimman huudon
        if bid_round == 1:
            print(f"Tallennetaan huuto: {bid}")
        if bid_round == 2:
            print(f"Tallennetaan korotus: {bid}")

    def bid_win(self, hand): # lisää tarjouskierroksen voittajalle kortit
        if hand == "1":
            self._bid_win_hand = 1
            #self._bid_loose_hand = 2
            for card in self.bid_cards:
                self.hand1.append(card)

        elif hand == "2":
            self._bid_win_hand = 2
            #self._bid_loose_hand = 1
            for card in self.bid_cards:
                self.hand2.append(card)
        else:
            print("Virhe: Ilmoita pelaaja: 1 tai 2")


    def play_card(self, card, hand):
        trump = False
        if len(self.played) == 2:
            if trump:
                self.compare_trump(self.played)
            self.compare(self.played)
            #self.tricks(card, hand)
            self.played = []
            
        
        self.played.append((card, hand))
    
        return self.played

    def tricks(self, card, win): 
        #print("moi")
        if win == 1:
            self.bag1.append(self.played[0])
            self.bag1.append(self.played[1])
        if win == 2:
            self.bag2.append(self.played[0])
            self.bag2.append(self.played[1])
        print(f"pussi 1: {self.bag1}")
        print(f"pussi 2: {self.bag2}")

    def compare(self, trick):  # ei valttia
        rank_order = {"6":1, "7":2, "8":3, "9":4, "J":5, "Q":6, "K":7, "10":8, "A":9}
        card1 = trick[0]
        card2 = trick[1]
        if card1[0][1] != card2[0][1]: #pelaajilla eri maata
            self.tricks(card1[0], card1[1])
        
        elif rank_order[card1[0][0]] > rank_order[card2[0][0]]:
            self.tricks(card1[0], card1[1])

        elif rank_order[card2[0][0]] > rank_order[card1[0][0]]:
            self.tricks(card2[0], card2[1])

        else:
            print("Tänne ei pitäisi päästä")
        
    def compare_trump(self, trick): # valtti olemassa
        pass
