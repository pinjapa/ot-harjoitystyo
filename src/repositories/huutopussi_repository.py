from database_connection import get_database_connection

class HuutopussiRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def _find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Game")

        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append((rows[0][1], "/", rows[0][2], "|", rows[0][3], "|", rows[0][4]))

        return result


    def _add_bid(self, bid, bid2):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Game (bid, raise, player1, player2) values (?, ?, ?, ?)",
            (bid, bid2, None, None)
        )

        self._connection.commit()

    def _add_points(self, bid, points1, points2):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Game (bid, raise, player1, player2) values (?, ?) WHERE bid = ? ",
            (points1, points2, bid)
        )

        self._connection.commit()


huutopussi_repository = HuutopussiRepository(get_database_connection())