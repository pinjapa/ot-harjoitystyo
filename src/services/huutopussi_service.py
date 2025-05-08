import random
from services.count_service import CountService
from services.compare_service import CompareService
from repositories.huutopussi_repository import huutopussi_repository

class HuutopussiService:
    """ Luokka, joka vastaa sovelluslogiikasta."""

    def __init__(self):
        #self._pack = []
        self.hand1 = []
        self.hand2 = []
        self.bid_cards = []
        self._bid_win_hand = None
        self.played = []
        self.suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
        #self.bag1 = []
        #self.bag2 = []
        self.compare = CompareService()
        #self.trump = False
        #self.rank_order = {"6":1, "7":2, "8":3, "9":4, "J":5, "Q":6, "K":7, "10":8, "A":9}
        self.count = CountService()
        #self.turn = 1
        self.bid = None
        self.bid2 = None
        self.huutopussi_repository = huutopussi_repository
        self.id = 0

    def create_pack(self):
        """Alustaa korttipakan luomalla jokaisen pelissä olevan kortin
        Args:
            ranks: Korttien arvojärjestys
        """
        pack = []
        ranks = ["6", "7", "8", "9", "J", "Q", "K", "10", "A"]
        for i in self.suits:
            for j in ranks:
                pack.append((j, i))
        self.deal_cards(pack)

    def deal_cards(self, pack):
        """Jakaa kortit kahdelle kädelle, ja huutopakkaan.
        """
        random.shuffle(pack)
        self.hand1 = pack[:13]
        self.hand2 = pack[13:26]
        self.bid_cards = pack[32:36]
        self.compare.hand1 = self.hand1
        self.compare.hand2 = self.hand2

    def bid_save(self, bid, lap):  # TODO, tallentaa korkeimman tarjouksen
        """Tallentaa korkeimman tarjouksen
            Ensimmäisellä kierroksella pelaajalle tallennetaan huuto
            Toisella kierroksella tallennetaan samalle pelaajalle korotus
        """
        if lap == 2:
            self.bid = int(bid)

        if lap == 3:
            self.bid2 = int(bid)
            self.id = self.huutopussi_repository.add_bid(self.bid, self.bid2)

    def bid_win(self, hand, lap): # lisää tarjouskierroksen voittajalle kortit
        """Lisää tarjouksen voittajalle huutopakan kortit,
        jos huuto valmis eli kierros 2.

        """
        if hand != 1 or hand != 2:
            print("Virhe: Ilmoita pelaaja: 1 tai 2") #exception tähän

        if lap == 2:
            if hand == "1":
                self._bid_win_hand = 1
                #self.turn = 1
                for card in self.bid_cards:
                    self.hand1.append(card)

            elif hand == "2":
                self._bid_win_hand = 2
                #self.turn = 2
                for card in self.bid_cards:
                    self.hand2.append(card)

    def play_card(self, card, hand):
        """Tarkistaa pelatun kortin.
        Tarjouskierroksen voittaneen poislaittamat korit
        lisätään hänelle itselleen.

        Args:
            card: Pelattu kortti
            hand: Kumpi pelaaja on pelannut kortin
        
        Returns:
            Pelatut kortit, jos liikaa kortteja palauttaa "Laita kortti pois ensin!"
        """

        if len(self.hand1) > 13:
            self.compare.bag1.append(card)
            self.hand1.remove(card)
            return "Laita kortti pois ensin!"

        if len(self.hand2) > 13:
            self.compare.bag2.append(card)
            self.hand2.remove(card)
            return "Laita kortti pois ensin!"

        self.played.append((card, hand))

        if len(self.played) == 2:
            self.compare.played = self.played
            result = self.compare.start_compare(card, hand)
            self.played = []
            #print(result)
            if result[0]is True:
                print("menee is true")
                self.count.last_trick(result[1])
                self.count.count_cards(self.compare.bag1, self.compare.bag2)
                self.check_bid()
                self.huutopussi_repository.add_points(
                    self.count.game_points1, self.count.game_points2, self.id)
                return "Peli loppui"
            #result = self.start_compare(card, hand)
            return result

        return self.played


    def check_rules(self, card2, hand):

        card1 = self.played[0][0]
        #print(card2[1], card1[1])
        if card2[1] != card1[1]:
            if hand == 1: #pelaaja1 laittanut toisen kortin
                for card in self.hand1: # olisiko toisella pelaajalla ollut samaa maata
                    if card[1] == card1[1] and card != card2:
                        return False
                return True

            # hand == 2: #pelaaja2 laittanut toisen kortin

            for card in self.hand2: # olisiko toisella pelaajalla ollut samaa maata
                if card[1] == card1[1] and card != card2:
                    return False
            return True

        return True

    def check_bid(self):
        if self._bid_win_hand == 1:
            if self.count.points1 > self.bid:
                self.count.game_points1 += self.bid
            else:
                self.count.points1 -= self.bid
            self.count.no_bid_player(2)

        else:
            if self.count.points2 > self.bid:
                self.count.game_points2 += self.bid
            else:
                self.count.game_points2 -= self.bid
            self.count.no_bid_player(1)
