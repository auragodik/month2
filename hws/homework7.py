import sqlite3

def create_table():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS books")
    cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                author TEXT,
                publication_year INTEGER,
                genre TEXT,
                number_of_pages INTEGER,
                number_of_copies INTEGER
            )
        """)
    conn.commit()
    conn.close()


def insert_books():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    books = [
        ("Wild East", "Saluki", 2023, "Album", 23, 1),
        ("Freerio", "OG Buda", 2021, "album", 17, 3),
        ("Freerio2", "OG Buda", 2023, "Album", 19, 4),
        ("Freerio3", "OG Buda", 2024, "Album", 18, 2),
        ("Ghetto Garden", "MAYOT", 2021, "Album", 17, 6),
        ("Heavy Metal", "9mice, kai angel", 2022, "Album", 6, 3),
        ("Heavy Metal2", "9mice, kai angel", 2024, "Album", 20, 7),
        ("damage", "kai angel", 2025, "Album", 20, 2),
        ("Hate love", "FACE", 2019, "Album", 15, 4),
        ("ASPHALT", "9mice", 2023, "Album", 14, 5)
    ]

    cur.executemany("""
            INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        """, books)
    conn.commit()
    conn.close()

def delete_book(book_name):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM books WHERE name = ?", (book_name,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_books()
    delete_book("Freerio2")
    print("Таблица создана, книги добавлены, одна книга удалена.")