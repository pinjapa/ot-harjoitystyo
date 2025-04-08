from services.huutopussi_service import HuutopussiService
from ui.bid_raise_ui import BidRaise
from tkinter import ttk, Button


class UI:

    def __init__(self, root):
        self._root = root
        self._game = None

    def start(self):
        self._game = HuutopussiService()

        heading_label = ttk.Label(
            master=self._root, text="Huutopussi kaksinpeli")
        heading_label.grid(row=0, column=2)

        bid_raise_elements = BidRaise(self._root, self._game)
        bid_raise_elements.create()

        self.show_cards()

    def show_cards(self):
        self._game.create_pack()
        self._game.deal_cards()

        column_1 = 4

        for i in self._game.hand1:
            self.button = Button(self._root, text=i, width=5)
            self.button['command'] = lambda binst=self.button: self.click(
                binst)
            self.button.grid(row=3, column=column_1)
            column_1 += 1

        column_1 = 4
        for i in self._game.hand2:
            self.button = Button(self._root, text=i, width=5)
            self.button['command'] = lambda binst=self.button: self.click(
                binst)
            self.button.grid(row=4, column=column_1)
            column_1 += 1

    def click(self, binst):
        binst.destroy()
