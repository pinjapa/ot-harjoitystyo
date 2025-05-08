
class CountService:
    """Pisteenlaskusta vastaava luokka"""
    def __init__(self):
        self.points1 = 0
        self.points2 = 0
        self.card_values = {"6":0, "7":0, "8":0, "9":0, "J":2, "Q":3, "K":4, "10":10, "A":11}
        self.game_points1 = 0
        self.game_points2 = 0

    def count_cards(self, bag1, bag2):
        """Laskee kerättyjen korttien tuottamat pisteet.
        
        Args:
            bag1: Pelaajan 1 keräämät tikit
            bag2: Pelaajan 2 keräämät tikit
        """
        for card in bag1:
            self.points1 += self.card_values[card[0]]

        for card in bag2:
            self.points2 += self.card_values[card[0]]

    def last_trick(self, winner):
        """Lisää viimeisen tikin voittajalle 20 pistettä.
        
        Args:
            winner: Viimeisen tikin saanut pelaaja.
        """
        if winner == 1:
            self.points1 += 20
        else:
            self.points2 += 20

    def trump_done(self, trump, turn):
        """Metodi, lisää valtin tehneelle valtista pisteet.
        
        Args:
            trump: Tehty valtti
            turn: Valtin tehnyt pelaaja
        """
        points = 0
        if trump == "\u2663":
            points = 60
        if trump == "\u2665":
            points = 100
        if trump == "\u2666":
            points = 80
        if trump == "\u2660":
            points = 40

        if turn == 1:
            self.points1 += points
        if turn == 2:
            self.points2 += points

    def no_bid_player(self, player):
        """Lisää ei-tarjouskierroksen voittajalle tämän keräämän pistemäärän.
        
        Args:
            player: Pelaaja, joka saa suorat pisteet.
        """
        if player == 1:
            self.game_points1 += self.points1

        else:
            self.game_points2 += self.points2
