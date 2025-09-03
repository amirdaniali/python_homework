# Amir Daniali
# Code the Dream Python 101
# Week 8

import pathlib
import sqlite3
import pandas as pd


# Task 3: I wrote classes instead of functions to make the program cleaner
# and follow OOP encapsulation using singleton/DAO design pattern.
class ConnectionManager:
    _instance = None

    def __new__(cls, db_path):
        """creates a singleton object, if it is not created,
        else returns the previous singleton object"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_connection(db_path)
        return cls._instance

    def _init_connection(self, db_path):
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = 1")
        # self.connection.commit()

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            ConnectionManager._instance = None


class PublishersRepository:
    """Data Access Repo for publishers"""

    def __init__(self, connection):
        self.conn = connection
        self._create_table()

    def _create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS publishers (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(50) NOT NULL UNIQUE
                       );"""
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table publishers: {e}")
        finally:
            cursor.close()

    def insert(self, name):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO publishers (name) VALUES (?);", (name,))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Publishers Insert Error: {e}")
        except sqlite3.Error as e:
            print(f"Publishers Insert Error: {e}")
        finally:
            cursor.close()

    def get_publisher_by_name(self, name):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM publishers WHERE name = ?;", (name,))
            result = cursor.fetchone()
            return result
        except sqlite3.Error as e:
            print(f"Publishers Select Error: {e}")
            return None
        finally:
            cursor.close()

    def get_all_publishers(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM publishers;")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Publishers Select Error: {e}")
            return []
        finally:
            cursor.close()


class MagazineRepository:
    def __init__(self, connection):
        self.conn = connection
        self._create_table()

    def _create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS magazines (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(50) NOT NULL UNIQUE,
                       publisher_id INTEGER NOT NULL REFERENCES publishers(id) ON DELETE CASCADE
                       )
            """
            )
            cursor.close()
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table magazines: {e}")

    def insert(self, name, publisher_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO magazines (name, publisher_id) VALUES (?, ?);",
                (name, publisher_id),
            )
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Magazines Insert Error: {e}")
        except sqlite3.Error as e:
            print(f"Magazines Insert Error: {e}")
        finally:
            cursor.close()

    def get_magazine_by_name(self, name):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE name = ?;", (name,))
            result = cursor.fetchone()
            return result
        except sqlite3.Error as e:
            print(f"Magazines Select Error: {e}")
            return None
        finally:
            cursor.close()

    def get_all_magazines(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM magazines;")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Magazines Select Error: {e}")
            return []
        finally:
            cursor.close()

    def get_all_magazines_by_publisher(self, publisher_id=None, publisher_name=None):
        """Turns out it doesn't require a join; A subquery works as well."""
        try:
            cursor = self.conn.cursor()
            if publisher_id:
                cursor.execute(
                    "SELECT * FROM magazines WHERE magazines.publisher_id = ?;",
                    (publisher_id,),
                )
                return cursor.fetchall()

            elif publisher_name:
                cursor.execute(
                    """SELECT * FROM magazines WHERE magazines.publisher_id = (
                    SELECT id FROM publishers WHERE name = ?);""",
                    (publisher_name,),
                )
                return cursor.fetchall()
            else:
                print(
                    "Error getting magazines by publisher; Publisher ID or Name must be Specified."
                )
        except sqlite3.Error as e:
            print(f"Magazines Select Error: {e}")
            return []
        finally:
            cursor.close()

    def get_all_magazines_sorted(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM magazines ORDER BY name ASC;")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Magazines Select Error: {e}")
            return []
        finally:
            cursor.close()


class SubscribersRepository:
    def __init__(self, connection):
        self.conn = connection
        self._create_table()

    def _create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS subscribers (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(150) NOT NULL, 
                       address VARCHAR(150) NOT NULL,
                       CONSTRAINT unique_name_address UNIQUE (name, address)
                       )
            """
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table subscribers: {e}")
        finally:
            cursor.close()

    def insert(self, name, address):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT OR IGNORE INTO subscribers (name, address) VALUES (?, ?);",
                (name, address),
            )
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Subscribers Insert Error: {e}")
        except sqlite3.Error as e:
            print(f"Subscribers Insert Error: {e}")
        finally:
            cursor.close()

    def get_subscriber_by_name(self, name):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM subscribers WHERE name = ?;", (name,))
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Subscribers Select Error: {e}")
            return None
        finally:
            cursor.close()

    def get_all_subscribers(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM subscribers;")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Subscribers Select Error: {e}")
            return []
        finally:
            cursor.close()


class SubscriptionsRepository:
    def __init__(self, connection):
        self.conn = connection
        self._create_table()

    def _create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS subscriptions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        subscriber_id INTEGER NOT NULL REFERENCES subscribers(id) ON DELETE CASCADE,
                        magazine_id INTEGER NOT NULL REFERENCES magazines(id) ON DELETE CASCADE,
                        expiration_date VARCHAR(20) NOT NULL
                       )
            """
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table subscriptions: {e}")
        finally:
            cursor.close()

    def insert(self, subscriber_id, magazine_id, expiration_date):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?);",
                (subscriber_id, magazine_id, expiration_date),
            )
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Subscriptions Insert Error: {e}")
        except sqlite3.Error as e:
            print(f"Subscriptions Insert Error: {e}")
        finally:
            cursor.close()

    def get_all_subscriptions(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM subscriptions;")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Subscriptions Select Error: {e}")
            return []
        finally:
            cursor.close()


if __name__ == "__main__":
    BASEDIR = pathlib.Path(__file__).parent.parent
    SQL_Path = BASEDIR / "db/magazines.db"

    # Task 1
    task_1_assignment = """Task 1: Create a New SQLite Database

    Within your python_homework repository, create an assignment8 git branch.
    Make the assignment8 folder the working folder. Within the assignment8 folder, create a file sql_intro.py.
    Write code to connect to a new SQLite database, ../db/magazines.db and to close the connection.
    Execute the script and confirm the database file is created. Note: All SQL statements should be executed within a try block, followed by a corresponing except block, because any SQL statement can cause an exception to be raised.
    """

    with sqlite3.connect(SQL_Path) as conn:
        print("Database created and connected successfully.")

    # Task 2
    task_2_assignment = """Task 2: Define Database Structure
    We have publishers that publish magazines.  Each publisher has a unique name, and so does each magazine.  There is a one-to-many relationship between publishers and magazines.  We also have subscribers, and each subscriber has a name and an address.  We have a many-to-many association between subscribers and magazines, because a subscriber may subscribe to several magazines, and a magazine may have many subscribers.  So, we have a join table called subscriptions.  The subscriptions table also stores the expiration_date (a string) for the subscription.  All the names, the address, and the expiration_date must be non-null.
    Think for a minute.  There is a one-to-many relationship between publishers and magazines.  Which table has a foreign key? Where does the foreigh key point?  How about the subscriptions table: What foreigh keys does it have?
    Add SQL statements to sql_intro.py that create the following tables:
        publishers
        magazines
        subscribers
        subscriptions Be sure to include the columns you need in each, with the right data types, with UNIQUE and NOT NULL constraints as needed, and with foreign keys as needed. You can reuse column names if you choose, i.e. you might have a name column for publishers and a name column for magazines. By the way, if you mess up this or the following steps, you can just delete db/magazines.db.
    Open the db/magazines.db file in VSCode to confirm that the tables are created.
        """

    with sqlite3.connect(SQL_Path) as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS publishers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50) NOT NULL UNIQUE)"""
            )
        except Exception as e:
            print("Error Creating the Publishers Table")
            print(e)

        try:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS magazines (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50) NOT NULL UNIQUE,
                        publisher_id INTEGER NOT NULL REFERENCES publishers(id) ON DELETE CASCADE)"""
            )
        except Exception as e:
            print("Error Creating the magazines Table")
            print(e)

        try:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS subscribers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(150) NOT NULL, 
                        address VARCHAR(150) NOT NULL,
                        CONSTRAINT unique_name_address UNIQUE (name, address) )"""
            )
        except Exception as e:
            print("Error Creating the Subscribers Table")
            print(e)

        try:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS subscriptions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            subscriber_id INTEGER NOT NULL REFERENCES subscribers(id) ON DELETE CASCADE,
                            magazine_id INTEGER NOT NULL REFERENCES magazines(id) ON DELETE CASCADE,
                            expiration_date VARCHAR(20) NOT NULL)"""
            )
        except Exception as e:
            print("Error Creating the Subscriptions Table")
            print(e)

    # Task 3
    task_3_assignment = """Task 3: Populate Tables with Data
    Add the following line to sql_intro.py, right after the statement that connects to the database:
    conn.execute("PRAGMA foreign_keys = 1")
    This line tells SQLite to make sure the foreign keys are valid.
    Create functions, one for each of the tables, to add entries. Include code to handle exceptions as needed, and to ensure that there is no duplication of information. The subscribers name and address columns don't have unique values -- you might have several subscribers with the same name -- but when creating a subscriber you should check that you don't already have an entry where BOTH the name and the address are the same as for the one you are trying to create.
    Add code to the main line of your program to populate each of the 4 tables with at least 3 entries. Don't forget the commit!
    Run the program several times. View the database to ensure that you are creating the right information, without duplication.
"""
    conn = ConnectionManager(db_path=SQL_Path).get_connection()

    # define DAOs
    publishers_repo = PublishersRepository(conn)
    magazine_repo = MagazineRepository(conn)
    subscribers_repo = SubscribersRepository(conn)
    subscriptions_repo = SubscriptionsRepository(conn)

    # Add publishers
    publishers_repo.insert(name="Python Media")
    publishers_repo.insert(name="JS Gurus")
    publishers_repo.insert(name="SQL Pro")

    # Add magazines
    magazine_repo.insert(
        name="Python Weekly",
        publisher_id=publishers_repo.get_publisher_by_name("Python Media")["id"],
    )
    magazine_repo.insert(
        name="Python Insiders",
        publisher_id=publishers_repo.get_publisher_by_name("Python Media")["id"],
    )
    magazine_repo.insert(
        name="JS Weekly",
        publisher_id=publishers_repo.get_publisher_by_name("JS Gurus")["id"],
    )

    # Add Subscribers
    subscribers_repo.insert(name="John Jackson", address="123 Drive, Atlanta, GA")
    subscribers_repo.insert(name="Jasdhir Diva", address="213 Drive, Atlanta, GA")
    subscribers_repo.insert(name="Alexa Smalls", address="321 Drive, Atlanta, GA")

    # Add Subscriptions
    subscriptions_repo.insert(
        subscriber_id=subscribers_repo.get_subscriber_by_name("John Jackson")[0]["id"],
        magazine_id=magazine_repo.get_magazine_by_name("Python Insiders")["id"],
        expiration_date="01-01-2030",
    )
    subscriptions_repo.insert(
        subscriber_id=subscribers_repo.get_subscriber_by_name("Alexa Smalls")[0]["id"],
        magazine_id=magazine_repo.get_magazine_by_name("Python Insiders")["id"],
        expiration_date="01-02-2030",
    )
    subscriptions_repo.insert(
        subscriber_id=subscribers_repo.get_subscriber_by_name("Jasdhir Diva")[0]["id"],
        magazine_id=magazine_repo.get_magazine_by_name("JS Weekly")["id"],
        expiration_date="01-03-2030",
    )

    # Task 4
    task_4_assignment = """Task 4: Write SQL Queries

    Write a query to retrieve all information from the subscribers table.
    Write a query to retrieve all magazines sorted by name.
    Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
    Add these queries to your script. For each, print out all the rows returned by the query.

    """

    # Write a query to retrieve all information from the subscribers table.
    print("\nSubscribers:\n")
    for row in subscribers_repo.get_all_subscribers():
        print(dict(row))

    # Write a query to retrieve all magazines sorted by name.
    print("\nMagazines:\n")
    for row in magazine_repo.get_all_magazines_sorted():
        print(dict(row))

    # Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
    print("\nMagazines By Python Media:\n")
    python_media_magazines = magazine_repo.get_all_magazines_by_publisher(
        publisher_name="Python Media"
    )
    for row in python_media_magazines:
        print(dict(row))
