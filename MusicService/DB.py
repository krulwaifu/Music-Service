import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\Users\super\PycharmProjects\MusicService\db.sqlite3"

    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
                                        user_id integer PRIMARY KEY,
                                        fname text NOT NULL,
                                        lname text NOT NULL,
                                        email text NOT NULL,
                                        password text NOT NULL,
                                    ); """

    sql_create_audio_table = """CREATE TABLE IF NOT EXISTS audio (
                                    audio_id integer PRIMARY KEY,
                                    file_name text NOT NULL,
                                    name text NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES user (user_id)
                                );"""
    sql_create_album_table = """CREATE TABLE IF NOT EXISTS album (
                                       id integer PRIMARY KEY,
                                       name text NOT NULL,
                                       FOREIGN KEY (user_id) REFERENCES user (user_id)
                                   );"""

    sql_create_album_audio_table = """CREATE TABLE IF NOT EXISTS album (
                                           FOREIGN KEY (audio_id) REFERENCES audio_id (audio_id)
                                           FOREIGN KEY (user_id) REFERENCES user (user_id)
                                       );"""
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()