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
            result.append((row[1], "/", row[2], "|", row[3], "|", row[4]))

        return result


    def add_bid(self, bid, bid2):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Game (bid, raise, player1, player2) values (?, ?, ?, ?)",
            (bid, bid2, None, None)
        )

        self._connection.commit()

        cursor = self._connection.cursor()

        cursor.execute("SELECT max(id) FROM Game")

        result = cursor.fetchone()

        return result[0]

    def add_points(self, points1, points2, id_row):
        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE Game SET player1 = ?, player2 = ? WHERE id = ?",
            (points1, points2, id_row)
        )

        self._connection.commit()


huutopussi_repository = HuutopussiRepository(get_database_connection())
