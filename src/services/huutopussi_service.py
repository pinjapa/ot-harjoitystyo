import random


class HuutopussiService: #sovelluslogiikka
    
    def __init__(self):
        self.pack = []
        self.hand1 = []
        self.hand2 = []
        self.out_of_game = [] #pirunpakka
        self.bid_cards = []

    def create_pack(self):      
        ranks = [6, 7, 8, 9, "J", "Q", "K", 10, "A"]
        suits = ["heart", "diamond", "club", "spade"]
        for i in suits:
            for j in ranks:
                self.pack.append((i,j))

    def deal_cards(self):
        random.shuffle(self.pack)
        self.hand1 = self.pack[:13]
        self.hand2 = self.pack[13:26]
        self.out_of_game = self.pack[26:32]
        self.bid_cards = self.pack[32:36]
