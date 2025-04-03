from services.huutopussi_service import HuutopussiService
from ui.bid_raise_ui import BidRaise
from tkinter import ttk

class UI:

    def __init__(self, root):
        self._root = root
        #self._entry = None
        self._game = None

    def start(self):
        self._game = HuutopussiService()
        heading_label = ttk.Label(master=self._root, text="Huutopussi kaksinpeli")

        self.show_cards()
        bid_raise_elements = BidRaise(self._root, self._game)
        bid_raise_elements.create()

        heading_label.grid(row=0, column=2, columnspan=4)
    
    def show_cards(self):
        self._game.create_pack()
        self._game.deal_cards()
        hand1 = ttk.Label(master=self._root, text=f"{self._game.hand1}")
        hand2 = ttk.Label(master=self._root, text=f"{self._game.hand2}")

        hand1.grid(row=4, column=4, columnspan=2)
        hand2.grid(row=5, column=4, columnspan=2)