import sqlite3

def connect():
    try:
        conn=sqlite3.connect("bhisi.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS names (unique_id INTEGER NOT NULL UNIQUE, name TEXT NOT NULL PRIMARY KEY)")
        cur.execute("CREATE TABLE IF NOT EXISTS winners (name TEXT NOT NULL PRIMARY KEY, winner_flag INTEGER)")
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print(error)
        conn.close()


def insertMultipleRecords(recordList):
    try:
        conn = sqlite3.connect('bhisi.db')
        cur = conn.cursor()
        sqlite_insert_query = "INSERT INTO names (unique_id,name) VALUES (?,?)"
        cur.executemany(sqlite_insert_query, recordList)
        conn.commit()
        print("Total", cur.rowcount, "Records inserted successfully")
        conn.commit()
        cur.close()
    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
        conn.close()    

   
def SingleInsert(unique_id,name):
    try:
        conn=sqlite3.connect("bhisi.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO names (unique_id,name) VALUES (?,?)",(unique_id,name))
        conn.commit()
        conn.close()
        view()
    except sqlite3.Error as error:
        print(error)
        conn.close()
   
    
def view():
    conn=sqlite3.connect("bhisi.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM names")
    rows=cur.fetchall()
    conn.close()
    return rows

def fetch():
    conn=sqlite3.connect("bhisi.db")
    cur=conn.cursor()
    cur.execute("SELECT name FROM names")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(unique_id="",name=""):
    conn=sqlite3.connect("bhisi.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM names WHERE unique_id=? OR name=?", (unique_id,name))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(unique_id):
    try:
        conn=sqlite3.connect("bhisi.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM names WHERE unique_id=?",(unique_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print(error)
        conn.close()


def update(unique_id,name):
    try:
        conn=sqlite3.connect("bhisi.db")
        cur=conn.cursor()
        cur.execute("UPDATE names SET name=? WHERE unique_id=?",(name,unique_id))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print(error)
        conn.close()
            
            
def delete_table():
    conn=sqlite3.connect("bhisi.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE names")
    conn.commit()
    conn.close()


def getLastUniqueID():
    conn=sqlite3.connect("bhisi.db")
    cur=conn.cursor()
    cur.execute("SELECT MAX(unique_id) FROM names")
    last_uid=cur.fetchone()
    conn.close()
    return last_uid


def getWinnerFlag():
    conn=sqlite3.connect("bhisi.db")
    cur=conn.cursor()
    cur.execute("SELECT name FROM names WHERE winner_flag = 1")
    rows=cur.fetchall()
    conn.close()
    return rows



