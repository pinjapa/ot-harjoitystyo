from database_connection import get_database_connection

class HuutopussiRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def find_all(self):
        pass


huutopussi_repository = HuutopussiRepository(get_database_connection())