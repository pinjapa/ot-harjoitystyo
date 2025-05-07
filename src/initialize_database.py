from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantataulun

    Args:
        connection: Tietokantayhteys Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists game;
    """)

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.

    Args:
        connection: Tietokantayhteys Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE game (
            bid text primary key,
            player1 integer,
            player2 interger
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