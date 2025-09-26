import sqlite3


def create_tables():
    conn.execute('DROP TABLE IF EXISTS students')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)
def add_students(name, age, city):
    conn.execute(
        'INSERT INTO students (name, age, city) VALUES (?, ?, ?)',
        (name, age, city)
    )
if __name__=='__main__':
    conn = sqlite3.connect('../database.db')
create_tables()
add_students('Nuradil', 12,'London')
