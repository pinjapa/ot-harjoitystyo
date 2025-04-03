from services.huutopussi_service import HuutopussiService
from tkinter import ttk


class BidRaise:

    def __init__(self, root, game):
        self._root = root
        self._game = game
        self._entry = None
        self.round = 1
        
    def create(self):
        self._entry = ttk.Entry(master=self._root)

        bid_ready_button = ttk.Button(
          master=self._root,
          text="Lukitse",
          command=self._ready_button_click
        )
        self.bid_button()
        bid_ready_button.grid(row=2, column=3)
        self._entry.grid(row=1, column=2)
    
    def bid_button(self):
        text = "Huuda"
        if self.round == 2:
            text = "Korota"

        bid_button = ttk.Button(
          master=self._root,
          text=text,
          command=self._bid_button_click
        )
        bid_button.grid(row=2, column=2)
    
    def _bid_button_click(self):
        self._bid_value = self._entry.get()
        if self.round == 1:
            bid_label = ttk.Label(master=self._root, text=f"Huuda: {self._bid_value}")
        
            bid_label.grid(row=0, column=0, columnspan=2)
        else: 
            bid_label = ttk.Label(master=self._root, text=f"Korota: {self._bid_value}")
            bid_label.grid(row=1, column=0, columnspan=2)
    
    def _ready_button_click(self):
        self._game.bid_phase(self._bid_value) 
        self.round = 2
        self.bid_button()