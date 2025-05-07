from database_connection import get_database_connection

class HuutopussiRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def _find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Game")

        rows = cursor.fetchall()
        result = []
        i = 0
        for row in rows:
            result.append((rows[i][1], "/", rows[i][2], "|", rows[i][3], "|", rows[i][4]))
            i += 1

        return result


    def _add_bid(self, bid, bid2):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Game (bid, raise, player1, player2) values (?, ?, ?, ?)",
            (bid, bid2, None, None)
        )

        self._connection.commit()

        cursor = self._connection.cursor()

        cursor.execute("SELECT max(id) FROM Game")

        result = cursor.fetchone()
        print(result[0])

        return result[0]

    def _add_points(self, points1, points2, id):
        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE Game SET player1 = ?, player2 = ? WHERE id = ?",
            (points1, points2, id)
        )

        self._connection.commit()


huutopussi_repository = HuutopussiRepository(get_database_connection())