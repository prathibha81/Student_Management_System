""" Database Module for Student Management System """
import sqlite3

def connect():
    return sqlite3.connect("sms.db")

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll_no TEXT UNIQUE,
        class TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS marks(
        mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        fa1 INTEGER, fa2 INTEGER, sa1 INTEGER,
        fa3 INTEGER, fa4 INTEGER, sa2 INTEGER,
        final INTEGER,
        grade TEXT,
        result TEXT,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
    """)

    conn.commit()
    conn.close()
