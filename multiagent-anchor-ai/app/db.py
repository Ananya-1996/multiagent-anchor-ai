import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
cur = conn.cursor()

# 📅 EVENTS
cur.execute("""
CREATE TABLE IF NOT EXISTS events(
    id INTEGER PRIMARY KEY,
    text TEXT,
    time TEXT
)
""")

# 📊 DASHBOARD
cur.execute("""
CREATE TABLE IF NOT EXISTS dashboard(
    id INTEGER PRIMARY KEY,
    mood TEXT,
    tasks_done INTEGER,
    streak INTEGER
)
""")

conn.commit()


# 📅 EVENTS
def save_event(text, time):
    cur.execute("INSERT INTO events(text,time) VALUES(?,?)", (text, time))
    conn.commit()


def get_events():
    return cur.execute("SELECT * FROM events").fetchall()


# 📊 DASHBOARD
def update_dashboard(mood=None, task_increment=0):
    row = cur.execute(
        "SELECT mood, tasks_done, streak FROM dashboard ORDER BY id DESC LIMIT 1"
    ).fetchone()

    if row:
        current_mood, tasks, streak = row
    else:
        current_mood, tasks, streak = "🙂 okay", 0, 1

    new_mood = mood if mood else current_mood
    new_tasks = tasks + task_increment

    cur.execute(
        "INSERT INTO dashboard(mood, tasks_done, streak) VALUES(?,?,?)",
        (new_mood, new_tasks, streak)
    )

    conn.commit()


def get_dashboard():
    row = cur.execute(
        "SELECT mood, tasks_done, streak FROM dashboard ORDER BY id DESC LIMIT 1"
    ).fetchone()

    return row if row else ("🙂 okay", 0, 1)
