import random
from services.count_service import CountService
from services.compare_service import CompareService
from repositories.huutopussi_repository import huutopussi_repository

class HuutopussiService:
    """ Luokka, joka vastaa sovelluslogiikasta."""

    def __init__(self):
        self.hand1 = []
        self.hand2 = []
        self.bid_cards = []
        self._bid_win_hand = None
        self.played = []
        self.bid = None
        self.bid2 = None
        self.suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
        self.compare = CompareService()
        self.count = CountService()
        self.huutopussi_repository = huutopussi_repository
        self.id = 0

    def create_pack(self):
        """Alustaa korttipakan luomalla jokaisen pelissä olevan kortin"""

        pack = []
        ranks = ["6", "7", "8", "9", "J", "Q", "K", "10", "A"]
        for i in self.suits:
            for j in ranks:
                pack.append((j, i))
        self.deal_cards(pack)

    def deal_cards(self, pack):
        """Jakaa kortit kahdelle kädelle, ja huutopakkaan.
        
        Args:
            pack: Korttipakka, josta jaetaan kortit.
        """

        random.shuffle(pack)
        self.hand1 = pack[:13]
        self.hand2 = pack[13:26]
        self.bid_cards = pack[32:36]
        self.compare.hand1 = self.hand1
        self.compare.hand2 = self.hand2

    def bid_save(self, bid, lap):
        """Tallentaa korkeimman tarjouksen.
        Ensimmäisellä kierroksella pelaajalle tallennetaan huuto.
        Toisella kierroksella tallennetaan samalle pelaajalle korotus.

        Args:
            bid: Huuto tai korotus on arvo, jonka pelaaja syöttää.
            lap: Kierros, joka kertoo onko kysessä huuto vai korotus.
        """
        if lap == 2:
            self.bid = int(bid)

        if lap == 3:
            self.bid2 = int(bid)
            self.id = self.huutopussi_repository.add_bid(self.bid, self.bid2)

    def bid_win(self, hand, lap):
        """Lisää tarjouksen voittajalle huutopakan kortit,
        jos huuto valmis eli kierros 2.

        Args:
            hand: Kertoo, kumpi pelaaja voitti huudon.
            lap: Argumentti, joka varmistaa, että huuto on oikea
        
        Returns:
            False, jos syöte on muuta kuin 1 tai 2, muutoin True.
        """
        if hand not in ("1", "2"):
            return False

        if lap == 1:
            if hand == "1":
                self._bid_win_hand = 1
                self.compare.turn = 1
                for card in self.bid_cards:
                    self.hand1.append(card)

            else:
                self._bid_win_hand = 2
                self.compare.turn = 2
                for card in self.bid_cards:
                    self.hand2.append(card)

        return True

    def play_card(self, card, hand):
        """Tarkistaa pelatun kortin.
        Tarjouskierroksen voittaneen poislaittamat korit
        lisätään hänelle itselleen.

        Args:
            card: Pelattu kortti
            hand: Kumpi pelaaja on pelannut kortin
        
        Returns:
            Pelatut kortit, jos liikaa kortteja palauttaa "Laita kortti pois ensin!"
            Jos kaikki kortit pelattu, palauttaa "Peli loppui!"
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
            result = self.compare.start_compare()
            self.played = []
            if result[0]is True:
                self.count.last_trick(result[1])
                self.count.count_cards(self.compare.bag1, self.compare.bag2)
                self.check_bid()
                self.huutopussi_repository.add_points(
                    self.count.game_points1, self.count.game_points2, self.id)
                self._reset()
                return "Peli loppui"
            return result

        return self.played

    def _reset(self):
        """Nollaa uuden kierroksen alussa tarvittavat arvot"""
        self.compare.bag1 = []
        self.compare.bag2 = []
        self.compare.trump = False
        self.count.points1 = 0
        self.count.points2 = 0

    def check_rules(self, card2, hand):
        """Tarkistaa maapakon eli onko pelattu samaa maata, jos sitä on kädessä.

        Args:
            card2: Jälkimmäiseksi pelattu kortti
            hand: Jälkimmäisen kortin pelaaja, 1 tai 2

        Returns:
            True, jos kortit on pelattu oikein, muutoin False.
        """

        card1 = self.played[0][0]
        if card2[1] != card1[1]:
            if hand == 1:
                for card in self.hand1:
                    if card[1] == card1[1] and card != card2:
                        return False
                return True

            for card in self.hand2:
                if card[1] == card1[1] and card != card2:
                    return False
            return True

        return True

    def check_bid(self):
        """Tarkastaa, saiko tarjouskierroksen voittanut,
        sen verran pisteitä, kun oli tarjonnut.
        Mikäli on, hän saa huutamansa pistemäärän, muutoin miinusta sen verran.
        """
        if self._bid_win_hand == 1:
            if self.count.points1 > self.bid2:
                self.count.game_points1 += self.bid2
            else:
                self.count.points1 -= self.bid2
            self.count.no_bid_player(2)

        else:
            if self.count.points2 > self.bid2:
                self.count.game_points2 += self.bid2
            else:
                self.count.game_points2 -= self.bid2
            self.count.no_bid_player(1)
