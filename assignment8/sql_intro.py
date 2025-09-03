import sqlite3
import pandas as pd

### Task1: Create a New SQLite Database

try:
    # Connect to magazines.db
    connection = sqlite3.connect("../db/magazines.db")
    connection.execute("PRAGMA foreign_keys = 1")  # enable foreign key enforcement
    cursor = connection.cursor()
    print("Database connected successfully!")

    ### Task2: Define Database Structure

    # Create publishers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)

    # Create magazines table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(id)
    );
    """)

    # Create subscribers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    );
    """)

    # Create subscriptions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id),
        UNIQUE(subscriber_id, magazine_id)
    );
    """)

    ### Task3: Populate Tables with Data

    def add_publisher(cursor, name):
        try:
            cursor.execute("INSERT OR IGNORE INTO publishers (name) VALUES (?)", (name,))
        except sqlite3.Error as e:
            print(f"Error adding publisher {name}: {e}")

    def add_magazine(cursor, name, publisher_id):
        try:
            cursor.execute("INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        except sqlite3.Error as e:
            print(f"Error adding magazine {name}: {e}")

    def add_subscriber(cursor, name, address):
        try:
            cursor.execute("SELECT id FROM subscribers WHERE name=? AND address=?", (name, address))
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        except sqlite3.Error as e:
            print(f"Error adding subscriber {name}: {e}")

    def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
        try:
            cursor.execute("INSERT OR IGNORE INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                       (subscriber_id, magazine_id, expiration_date))
        except sqlite3.Error as e:
            print(f"Error adding subscription: {e}")

    # Populate publishers
    add_publisher(cursor, "Time Inc.")
    add_publisher(cursor, "Condé Nast")
    add_publisher(cursor, "Hearst Communications")

    # Get publisher IDs
    cursor.execute("SELECT id FROM publishers WHERE name='Time Inc.'")
    time_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM publishers WHERE name='Condé Nast'")
    conde_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM publishers WHERE name='Hearst Communications'")
    hearst_id = cursor.fetchone()[0]

    # Populate magazines
    add_magazine(cursor, "Time", time_id)
    add_magazine(cursor, "Vogue", conde_id)
    add_magazine(cursor, "Cosmopolitan", hearst_id)

    # Populate subscribers
    add_subscriber(cursor, "Alice Smith", "123 Main St")
    add_subscriber(cursor, "Bob Johnson", "456 Oak Ave")
    add_subscriber(cursor, "Charlie Brown", "789 Pine Rd")

    # Get subscriber IDs
    cursor.execute("SELECT id FROM subscribers WHERE name='Alice Smith'")
    alice_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM subscribers WHERE name='Bob Johnson'")
    bob_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM subscribers WHERE name='Charlie Brown'")
    charlie_id = cursor.fetchone()[0]

    # Get magazine IDs
    cursor.execute("SELECT id FROM magazines WHERE name='Time'")
    time_mag_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM magazines WHERE name='Vogue'")
    vogue_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM magazines WHERE name='Cosmopolitan'")
    cosmo_id = cursor.fetchone()[0]

    # Populate subscriptions
    add_subscription(cursor, alice_id, time_mag_id, "2025-12-31")
    add_subscription(cursor, bob_id, vogue_id, "2025-11-30")
    add_subscription(cursor, charlie_id, cosmo_id, "2025-10-15")
    add_subscription(cursor, alice_id, vogue_id, "2025-12-15")  # multiple subscriptions

    # Commit all changes
    connection.commit()
    print("Tables created and data populated successfully!")

    ### Task4: Write SQL Queries

    print("\n--- All Subscribers ---")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    print("\n--- All Magazines Sorted by Name ---")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for row in cursor.fetchall():
        print(row)

    print("\n--- Magazines for Publisher 'Condé Nast' ---")
    cursor.execute("""
        SELECT magazines.id, magazines.name, publishers.name
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.id
        WHERE publishers.name = ?
    """, ("Condé Nast",))
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    if 'connection' in locals():
        connection.close()
        print("Database connection closed.")
