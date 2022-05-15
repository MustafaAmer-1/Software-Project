from . import storage_wrapper

db_conn = storage_wrapper.db_conn

def choose_type(record):
    if (record):
            cur = db_conn.cursor()
            cur.execute('SELECT * FROM Manager WHERE NID = %s' , (record , ))
            r1 = cur.fetchone()
            if r1:
                return 1
            cur.execute('SELECT * FROM Clerk WHERE NID = %s' , (record , ))
            r1 = cur.fetchone()
            if r1:
                return 2
            cur.execute('SELECT * FROM User WHERE NID = %s' , (record , ))
            r1 = cur.fetchone()
            if r1:
                return 3
    return 0

def get_credientials(username):
        cur = db_conn.cursor()
        cur.execute('SELECT * FROM Person WHERE Email=%s', (username, ))
        record = cur.fetchone()
        return record