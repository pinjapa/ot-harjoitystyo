import random

class HuutopussiService:  # sovelluslogiikka

    def __init__(self):
        self.pack = []
        self.hand1 = []
        self.hand2 = []
        self.out_of_game = []  # pirunpakka
        self.bid_cards = []
        self.played = []
        self.bag1 = []
        self.bag2 = []


    def create_pack(self):
        ranks = [6, 7, 8, 9, "J", "Q", "K", 10, "A"]
        self.suits = ["heart", "diamond", "club", "spade"]
        for i in self.suits:
            for j in ranks:
                self.pack.append((i, j))

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
            self.bid_win_hand = 1
            self.bid_loose_hand = 2
            for card in self.bid_cards:
                self.hand1.append(card)
        
        elif hand == "2":
            self.bid_win_hand = 2
            self.bid_loose_hand = 1
            for card in self.bid_cards:
                self.hand2.append(card)
        else:
            print("Virhe: Ilmoita pelaaja: 1 tai 2")
        

    def play_card(self, card):
        if len(self.played) >= 2:
            self.played = []
        self.played.append(card)
        
        return self.played
    
    def tricks(self, card, hand):
        if hand == 1:
            self.bag1.append(card)
        if hand == 2:
            self.bag2.append(card)
        print(f"pussi 1: {self.bag1}")
        print(f"pussi 2: {self.bag2}")
        #while len(self.bid_win_hand) > len(self.bid_loose_hand):
            #self.bag
    
