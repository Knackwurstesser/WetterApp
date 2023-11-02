import sqlite3

def connect():
    conn = sqlite3.connect("orte.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ort (id INTEGER PRIMARY KEY, Ort TEXT, Longitude TEXT, Latitude TEXT)")
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("orte.db")
    cur = conn.cursor()
    cur.execute(("SELECT * FROM ort"))
    rows = cur.fetchall()
    conn.close()
    return rows

def cords(ort):
    conn = sqlite3.connect("orte.db")
    cur = conn.cursor()
    cur.execute('SELECT Latitude, Longitude FROM ort WHERE ort = ?',(ort,))
    rows = cur.fetchall()
    conn.close()
    return rows
