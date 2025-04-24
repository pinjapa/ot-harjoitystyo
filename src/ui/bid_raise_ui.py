from tkinter import ttk


class BidRaise:

    def __init__(self, root, game):
        self._root = root
        self._game = game
        self._entry = None
        self.round = 0
        self.bid_ready = False

    def create(self):

        self._bid_entry = ttk.Entry(master=self._root)
        self._bid_entry.grid(row=1, column=1)
        self._bid_win = ttk.Entry(master=self._root)
        self._bid_win.grid(row=2, column=3)

        bid_ready_button = ttk.Button(
            master=self._root,
            text="Lukitse",
            command=self._lock_button_click
        )
        bid_ready_button.grid(row=2, column=2)

        self.bid_button()

    def bid_button(self):
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
        self.round += 1
        self.bid_winner = self._bid_win.get()
        self._game.bid_win(self.bid_winner)  #kumman pelaajan käteen lisätään kortit
        print(f"Huudon voitti pelaaja {self.bid_winner}")
        self._game.bid_save(self._bid_value, self.round) # tallentaa
        
        print(f"Kierros: {self.round}")
        self.bid_button()