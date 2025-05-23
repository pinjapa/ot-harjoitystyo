from tkinter import ttk, Button


class BidRaise:
    """ Luokka, joka vastaa tarjouskierroksen
    käyttöliittymän komponenttien toteutuksesta
    """

    def __init__(self, root, game):
        """ Konstruktori

        Args:
            root: Käyttöliittymän kehys juuri
            game: HuutopussiService peli sovelluslogiikka
        """
        self._root = root
        self._game = game
        self._entry = None
        self.round = 1

    def create(self):
        """Luo tarjouskierroksen elementit."""

        self._bid_entry = ttk.Entry(master=self._root)
        self._bid_entry.grid(row=1, column=1)

        bid_win_label = ttk.Label(
            master=self._root, text="Kumpi voitti huudon? Kirjoita 1 tai 2")
        bid_win_label.grid(row=3, column=1)
        
        self._bid_win = ttk.Entry(master=self._root)
        self._bid_win.grid(row=4, column=1)

        lock_button = Button(self._root, text="Lukitse")
        lock_button['command'] = lambda binst=lock_button: self._lock_button_click(
                binst)
        lock_button.grid(row=5, column=1)

        self._bid_button()

    def _bid_button(self):
        """Nappi, jolla päivitetään huuto tai korotus"""
        text = ""
        if self.round <= 1:
            text = "Huuda"

        if self.round == 2:
            text = "Korota" 

        _bid_button = ttk.Button(
            master=self._root,
            text=text,
            command=self._bid_button_click
        )
        _bid_button.grid(row=2, column=1)

    def _bid_button_click(self):
        """ Huutonapin painalluksesta vastaava metodi.
        Ensimmäisellä kierroksella kyseessä on huuto.
        Toisella kierroksella kyseessä on korotus.
        """
        self._bid_value = self._bid_entry.get()
        if self.round <= 1:
            self.bid_label = ttk.Label(
                master=self._root, text=f"Huuto: {self._bid_value}")
            self.bid_label.grid(row=1, column=0)

        elif self.round == 2:
            self.bid_label = ttk.Label(
                master=self._root, text=f"Korotus: {self._bid_value}")
            self.bid_label.grid(row=2, column=0)

    def _lock_button_click(self, binst):
        """Lukitsee huudon/korotuksen.
        Päivittää lopuksi huuto/korotus napin.

        Args:
            binst: kertoo mikä nappi tuhotaan
        """
       
        self.bid_winner = self._bid_win.get()
        if self._game.bid_win(self.bid_winner, self.round) is True:
            self.round += 1
            self._game.bid_save(self._bid_value, self.round)
        
        self._bid_button()
        if self.round == 3:
            binst.destroy()