from services.huutopussi_service import HuutopussiService
from tkinter import ttk

class UI:

    def __init__(self, root):
        self._root = root
        self._entry = None
        self._game = None
        self.round = 1

    def start(self):
        self._game = HuutopussiService()
        heading_label = ttk.Label(master=self._root, text="Huutopussi kaksinpeli")
        
        self._entry = ttk.Entry(master=self._root)

        self.show_cards()
        self.bid_button()

        bid_ready_button = ttk.Button(
          master=self._root,
          text="Lukitse",
          command=self._ready_button_click
        )

        heading_label.grid(row=0, column=2, columnspan=4)
        self._entry.grid(row=1, column=2)
        bid_ready_button.grid(row=2, column=3)

    
    def show_cards(self):
        self._game.create_pack()
        self._game.deal_cards()
        hand1 = ttk.Label(master=self._root, text=f"{self._game.hand1}")
        hand2 = ttk.Label(master=self._root, text=f"{self._game.hand2}")

        hand1.grid(row=4, column=4, columnspan=2)
        hand2.grid(row=5, column=4, columnspan=2)
    
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

    
