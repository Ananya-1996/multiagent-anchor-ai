
import sqlite3
conn=sqlite3.connect("data.db",check_same_thread=False)
cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, text TEXT, time TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS memory(id INTEGER PRIMARY KEY, text TEXT)")
conn.commit()

def save_event(text,time):
    cur.execute("INSERT INTO events(text,time) VALUES(?,?)",(text,time))
    conn.commit()

def get_events():
    return cur.execute("SELECT * FROM events").fetchall()

def save_memory(text):
    cur.execute("INSERT INTO memory(text) VALUES(?)",(text,))
    conn.commit()

def get_last_memory():
    res=cur.execute("SELECT text FROM memory ORDER BY id DESC LIMIT 1").fetchone()
    return res[0] if res else None
