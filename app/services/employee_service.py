from . import storage_wrapper

db_conn = storage_wrapper.db_conn

def add_clerk(NID, clerkName, phone, Email, BD, Gender, password, station, start_time, end_time):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Person WHERE NID = %s", (NID, ))
    VerifyNID = cur.fetchall()
    cur.execute("SELECT * FROM Person WHERE Email = %s", (Email, ))
    VerifyEmail = cur.fetchall()
    if len(VerifyNID) != 0:
        raise ValueError("National ID already exists")
    elif len(VerifyEmail) != 0:
        raise ValueError("Email already exists")
    else:
        cur.execute('INSERT INTO Person VALUES ( %s, %s, %s, %s, %s, %s, %s)' , (NID, clerkName, phone, Email, BD, Gender, password))
        cur.execute('insert into Clerk(Station, Start_time, End_time, NID) values(%s, %s, %s, %s)' , (station, start_time, end_time, NID))
        db_conn.commit()
    cur.close()
    