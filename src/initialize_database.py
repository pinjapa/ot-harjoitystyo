from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantataulun

    Args:
        connection: Tietokantayhteys Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists Game;
    """)

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.

    Args:
        connection: Tietokantayhteys Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE Game (
            id INTEGER PRIMARY KEY,
            bid TEXT,
            raise TEXT,
            player1 INTEGER,
            player2 INTEGER
        );
    """)

    connection.commit()


def initialize_database():
    """Luo tietokantataulut."""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()