from services.huutopussi_service import HuutopussiService
from ui.bid_raise_ui import BidRaise
from tkinter import ttk, Button


class UI:

    def __init__(self, root):
        self._root = root
        self._game = None
        

    def start(self):
        self._root.geometry("1500x300")
        self._game = HuutopussiService()

        heading_label = ttk.Label(
            master=self._root, text="Huutopussi kaksinpeli")
        heading_label.grid(row=0, column=2)

        self.bid_raise_elements = BidRaise(self._root, self._game)
        self.bid_raise_elements.create()
        
        self._game.create_pack()
        self._game.deal_cards()
        self.show_cards()
        self.refresh_cards()

    def show_cards(self):
        column_1 = 4

        for card in self._game.hand1:
            self.button = Button(self._root, text=card, width=5)
            self.button['command'] = lambda binst=self.button, c=card: self.click(
                binst, c)
            self.button.grid(row=3, column=column_1)
            column_1 += 1

        column_1 = 4
        for card in self._game.hand2:
            self.button = Button(self._root, text=card, width=5)
            self.button['command'] = lambda binst=self.button, c=card: self.click(
                binst, c)
            self.button.grid(row=4, column=column_1)
            column_1 += 1
    
    def refresh_cards(self):
        refresh_button = ttk.Button(
            master=self._root,
            text="Huuto valmis",
            command=self.refresh_click
        )
        refresh_button.grid(row=4, column=2)
    
    
    def refresh_click(self):
        self.show_cards()
    
    
    def click(self, binst, card):
        self.played_cards(card)
        binst.destroy()
    
    def played_cards(self, card):
        played_label = ttk.Label(
            master=self._root, text="Tikki")
        played_label.grid(row=5, column=2)

        cards_label = ttk.Label(
          master=self._root, text=self._game.play_card(card))
        cards_label.grid(row=6,column=2)
        
