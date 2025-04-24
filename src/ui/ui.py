from services.huutopussi_service import HuutopussiService
from ui.bid_raise_ui import BidRaise
from tkinter import ttk, Button


class UI:

    def __init__(self, root):
        self._root = root
        self._game = None
        

    def start(self):
        self._root.geometry("1800x300")
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
            self.button['command'] = lambda binst=self.button, c=card, hand=1: self.click(
                binst, c, hand)
            self.button.grid(row=3, column=column_1)
            column_1 += 1

        column_1 = 4
        for card in self._game.hand2:
            self.button = Button(self._root, text=card, width=5)
            self.button['command'] = lambda binst=self.button, c=card, hand=2: self.click(
                binst, c, hand)
            self.button.grid(row=4, column=column_1)
            column_1 += 1
    
    def click(self, binst, card, hand):
        self.played_cards(card, hand)
        #self._game.tricks(card, hand)
        binst.destroy()
    
    def refresh_cards(self):
        refresh_button = ttk.Button(
            master=self._root,
            text="Huuto valmis",
            command=self.refresh_click
        )
        refresh_button.grid(row=4, column=2)
    
    def refresh_click(self):
        column = 17
        row = 3
        if self._game._bid_win_hand == 2:
            row = 4

        for card in self._game.bid_cards:
            self.button = Button(self._root, text=card, width=5)
            self.button['command'] = lambda binst=self.button, c=card, hand=self._game._bid_win_hand: self.click(
                binst, c, hand)
            self.button.grid(row=row, column=column)
            column += 1
        self.trumps()
    
    def played_cards(self, card, hand):
        played_label = ttk.Label(
            master=self._root, text="Tikki")
        played_label.grid(row=5, column=2)

        cards_label = ttk.Label(
          master=self._root, text=self._game.play_card(card, hand))
        cards_label.grid(row=6,column=2)
        
    def trumps(self):
        column = 4
        for suit in self._game.suits:
            trump_button = Button(self._root, text=suit, width=5)
            trump_button['command'] =lambda binst=trump_button, suit=suit: self.trump_click(
                binst, suit)
            trump_button.grid(row=7, column=column)
            column += 1
    
    def trump_click(self, binst, suit):
        print(suit)
        binst.destroy()