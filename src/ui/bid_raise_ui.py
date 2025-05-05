from tkinter import ttk


class BidRaise:
    """ Luokka, joka vastaa tarjouskierroksen
    käyttöliittymän komponenttien toteutuksesta
    """

    def __init__(self, root, game):
        """ Konstruktori

        Args:
            root: Käyttöliittymän kehys juuri
            game: HuutopussiService peli
        """
        self._root = root
        self._game = game
        self._entry = None
        self.round = 1
        self.bid_ready = False

    def create(self):
        """Luo peruselementit ikkunan vasempaan yläkulmaan.
        """
        self._bid_entry = ttk.Entry(master=self._root)
        self._bid_entry.grid(row=1, column=1)

        bid_win_label = ttk.Label(
            master=self._root, text="Kumpi voitti huudon? Kirjoita 1 tai 2")
        bid_win_label.grid(row=3, column=1)
        
        self._bid_win = ttk.Entry(master=self._root)
        self._bid_win.grid(row=4, column=1)

        lock_button = ttk.Button(
            master=self._root,
            text="Lukitse",
            command=self._lock_button_click
        )
        lock_button.grid(row=5, column=1)

        self.bid_button()

    def bid_button(self):
        """Nappi, jolla päivitetään huuto tai korotus"""
        text = ""
        if self.round <= 1:
            text = "Huuda"

        if self.round == 2:
            text = "Korota" 

        bid_button = ttk.Button(
            master=self._root,
            text=text,
            command=self._bid_button_click
        )
        bid_button.grid(row=2, column=1)

    def _bid_button_click(self):
        """ Huutonapin painalluksesta vastaava metodi.
        Ensimmäisellä kierroksella kyseessä on huuto.
        Toisella kierroksella kysessä on korotus.
        """
        self._bid_value = self._bid_entry.get()
        if self.round <= 1:
            bid_label = ttk.Label(
                master=self._root, text=f"Huuto: {self._bid_value}")
            bid_label.grid(row=1, column=0)

        elif self.round == 2:
            bid_label = ttk.Label(
                master=self._root, text=f"Korotus: {self._bid_value}")
            bid_label.grid(row=2, column=0)

    def _lock_button_click(self):
        """Lukitsee huudon/korotuksen.
        Päivittää lopuksi huuto/kortus napin.
        """
        self.round += 1
        self.bid_winner = self._bid_win.get()
        self._game.bid_win(self.bid_winner, self.round)  # kumman pelaajan käteen lisätään kortit
        self._game.bid_save(self._bid_value, self.round) # tallentaa
        
        self.bid_button()