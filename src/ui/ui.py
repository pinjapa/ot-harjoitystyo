from services.huutopussi_service import HuutopussiService

class UI:

    def __init__(self):
        pass

    def start(self):
        game = HuutopussiService()
        game.create_pack()
        game.deal_cards()
        print("Kortit on jaettu")