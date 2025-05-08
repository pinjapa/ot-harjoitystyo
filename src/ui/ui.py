from services.huutopussi_service import HuutopussiService
from ui.bid_raise_ui import BidRaise
from tkinter import ttk, Button, N, CENTER, NE

class UI:

    def __init__(self, root):
        self._root = root
        self._game = None
        self._game = HuutopussiService()

    def start(self):
        self._root.geometry("1800x300")
        heading_label = ttk.Label(
            master=self._root, text="Huutopussi kaksinpeli")
        heading_label.place(relx=0.5, rely=0.0, anchor=N)

        game_state_label = ttk.Label(
            master=self._root, text="Peli tilanne: ")
        game_state_label.grid(row=3, column=20)
        game_state_label.place(relx=0.9, rely=0.2, anchor=NE)

        self.cards_label = ttk.Label(
            master=self._root, text="")
        self.cards_label.place(relx=0.5, rely=0.7, anchor=CENTER)

        game_state_refresh_button = ttk.Button(
            master=self._root,
            text="Päivitä",
            command=self._refresh_game_state_click
        )
        game_state_refresh_button.place(relx=0.95, rely=0.2, anchor=NE)

        self.bid_raise_elements = BidRaise(self._root, self._game)
        self.bid_raise_elements.create()
        self.turn_label()

        self._game.create_pack()
        #self._game.deal_cards()
        self.show_cards()
        self.refresh_cards()

    def show_cards(self):
        player1_label = ttk.Label(
            master=self._root, text="Pelaaja 1:")
        player1_label.grid(row=2, column=4)
        column_1 = 4

        for card in self._game.hand1:
            self.button = Button(self._root, text=card, width=5)
            self.button['command'] = lambda binst=self.button, c=card, hand=1: self.click(
                binst, c, hand)
            self.button.grid(row=3, column=column_1)
            column_1 += 1
        
        player2_label = ttk.Label(
            master=self._root, text="Pelaaja 2: ")
        player2_label.grid(row=4, column=4)
        column_1 = 4

        for card in self._game.hand2:
            self.button = Button(self._root, text=card, width=5)
            self.button['command'] = lambda binst=self.button, c=card, hand=2: self.click(
                binst, c, hand)
            self.button.grid(row=5, column=column_1)
            column_1 += 1
        
        played_label = ttk.Label(
            master=self._root, text="Tikki")
        played_label.grid(row=8, column=2)
        played_label.place(relx=0.5, rely=0.6, anchor=CENTER)

    def turn_label(self):
        self.turn = ttk.Label(
            master=self._root, text=f"Pelaajan {self._game.compare.turn} vuoro")
        self.turn.grid(row=5, column=2)
        self.turn.place(relx=0.5, rely=0.5, anchor=CENTER)

    def click(self, binst, card, hand):
        

        if len(self._game.played) == 0:
            
            self._game.play_card(card, hand)
            #text = self._game.played[0][0]
            self.cards_label.config(text=self._game.played)
            binst.destroy()

        

        elif len(self._game.played) == 1:
            correct_suit = self._game.check_rules(card, hand)
            if correct_suit == True:
                result = self._game.play_card(card, hand)
                print(result)
                if result == "Peli loppui":
                    self.cards_label.config(text="Kierros loppui!")
                    self.new_game()
                else:
                    self.cards_label.config(
                        text=f"{result[0][0]} {result[0][1]} | {result[1][0]} {result[1][1]}")
                binst.destroy()


        #result = self._game.play_card(card, hand)
        
        #cards_label = ttk.Label(
            #master=self._root, text=text)
        #cards_label.grid(row=9,column=2)
        #cards_label.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        self.turn.config(text=f"Pelaajan {self._game.compare.turn} vuoro")

    def refresh_cards(self):
        refresh_button = Button(self._root, text="Huuto valmis")
        refresh_button['command'] = lambda binst=refresh_button: self.refresh_click(
                binst)
        refresh_button.grid(row=6, column=1)
        self.turn.config(text=f"Pelaajan {self._game.compare.turn} vuoro")
    
    def _refresh_game_state_click(self):
        all = self._game.huutopussi_repository._find_all()
        #print(all)
        pos = 0.3
        for row in all:
            state_update = ttk.Label(
                master=self._root, text=row)
            state_update.place(relx=0.95, rely=pos, anchor=NE)
            pos += 0.1


    def refresh_click(self, binst):
        column = 17
        row = 3
        if self._game._bid_win_hand == 2:
            row = 5

        for card in self._game.bid_cards:
            self.button = Button(self._root, text=card, width=5)
            self.button['command'] = lambda binst=self.button, c=card, hand=self._game._bid_win_hand: self.click(
                binst, c, hand)
            self.button.grid(row=row, column=column)
            column += 1
        self.trumps()
        binst.destroy()
        
    def trumps(self):
        trump_label = ttk.Label(
            master=self._root, text="Tee valtti:")
        trump_label.grid(row=6, column=4)
        column = 4
        for suit in self._game.suits:
            trump_button = Button(self._root, text=suit, width=5)
            trump_button['command'] =lambda binst=trump_button, suit=suit: self.trump_click(
                binst, suit)
            trump_button.grid(row=7, column=column)
            column += 1
    
    def trump_click(self, binst, suit):
        self._game.compare.trump = suit
        self._game.count.trump_done(suit, self._game.compare.turn)
        binst.destroy()

    def new_game(self):
        self.new_game_button = Button(self._root, text="Uusi peli", width=5)
        self.new_game_button['command'] = lambda binst=self.new_game_button: self.new_game_click(
            binst)
        self.new_game_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    
    def new_game_click(self, binst):
        self.start()
        binst.destroy()