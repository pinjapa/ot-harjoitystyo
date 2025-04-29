import random
#from services.count_service import CountService

class HuutopussiService:
    """ Luokka, joka vastaa sovelluslogiikasta."""
    
    def __init__(self):
        self.pack = []
        self.hand1 = []
        self.hand2 = []
        self.bid_cards = []
        self._bid_win_hand = None
        self.played = []
        self.suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
        self.bag1 = []
        self.bag2 = []
        self.trump = False
        self.rank_order = {"6":1, "7":2, "8":3, "9":4, "J":5, "Q":6, "K":7, "10":8, "A":9}

    def create_pack(self):
        """Alustaa korttipakan luomalla jokaisen pelissä olevan kortin
        Args:
            ranks: Korttien arvojärjestys
        """
        ranks = ["6", "7", "8", "9", "J", "Q", "K", "10", "A"]
        for i in self.suits:
            for j in ranks:
                self.pack.append((j, i))

    def deal_cards(self):
        """Jakaa kortit kahdelle kädelle, ja huutopakkaan.
        """
        random.shuffle(self.pack)
        self.hand1 = self.pack[:13]
        self.hand2 = self.pack[13:26]
        self.bid_cards = self.pack[32:36]

    def bid_save(self, bid, lap):  # TODO, tallentaa korkeimman tarjouksen
        """Tallentaa korkeimman tarjouksen
            Ensimmäisellä kierroksella pelaajalle tallennetaan huuto
            Toisella kierroksella tallennetaan samalle pelaajalle korotus
        """
        if lap == 1:
            print(f"Tallennetaan huuto: {bid}")
        if lap == 2:
            print(f"Tallennetaan korotus: {bid}")

    def bid_win(self, hand, lap): # lisää tarjouskierroksen voittajalle kortit
        """Lisää tarjouksen voittajalle huutopakan kortit,
        jos huuto valmis eli kierros 2.

        """
        if lap == 2:
            if hand == "1":
                self._bid_win_hand = 1
                for card in self.bid_cards:
                    self.hand1.append(card)

            elif hand == "2":
                self._bid_win_hand = 2
                for card in self.bid_cards:
                    self.hand2.append(card)
            else:
                print("Virhe: Ilmoita pelaaja: 1 tai 2")

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
            self.compare_suits(self.played[0], self.played[1])
            self.played = []

        self.played.append((card, hand))

        return self.played

    def compare_suits(self, card1, card2):  # ei valttia
        """Vertailee, ovatko kortit samaa maata.

        Args:
            card1: Kahdesta kortista ensin pelattu, ja kumpi pelaaja
            card2: Toiseksi pelattu kortti, ja sen pelaaja
        """
        if card1[0][1] != card2[0][1]: #pelaajilla eri maata
            self.tricks(card1[1])
        else:
            self.compare_value(card1, card2)

    def compare_value(self, card1, card2):
        """ Vertailee, kumpi korteista on suurempi.

        Args:
            card1: Kahdesta kortista ensin pelattu, ja kumpi pelaaja
            card2: Toiseksi pelattu kortti, ja sen pelaaja
        """
        if self.rank_order[card1[0][0]] > self.rank_order[card2[0][0]]:
            self.tricks(card1[1])

        if self.rank_order[card2[0][0]] > self.rank_order[card1[0][0]]:
            self.tricks(card2[1])

    def compare_trump(self, card1, card2):
        """ Vertailee kortteja, kun valtti on olemassa.
            
        Args:
            card1: Kahdesta kortista ensin pelattu, ja kumpi pelaaja
            card2: Toiseksi pelattu kortti, ja sen pelaaja
        """
        if card1[0][1] != self.trump:
            if card2[0][1] != self.trump:
                self.compare_suits(card1, card2)

        elif card1[0][1] == self.trump:
            if card2[0][1] != self.trump:
                self.tricks(card1[1])
            elif card2[0][1] == self.trump:
                self.compare_value(card1, card2)

    def tricks(self, win):
        """ Kumman pelaajan kortti on suurempi, sen "pussiin" listään kääntö.

        Args:
            win: Kumman pelaajan kortti on suurempi.
        """
        if win == 1:
            self.bag1.append(self.played[0][0])
            self.bag1.append(self.played[1][0])
        if win == 2:
            self.bag2.append(self.played[0][0])
            self.bag2.append(self.played[1][0])
