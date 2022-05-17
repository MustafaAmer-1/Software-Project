from . import storage_wrapper

db_conn = storage_wrapper.db_conn

def register_user(NID, full_name, phone_no, email, DOB, gender, password):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Person WHERE NID = %s", (NID, ))
    VerifyNID = cur.fetchall()
    cur.execute("SELECT * FROM Person WHERE Email = %s", (email, ))
    VerifyEmail = cur.fetchall()
    if len(VerifyNID) != 0:
        raise ValueError("National ID already exists")
    elif len(VerifyEmail) != 0:
        raise ValueError("Email already exists")
    else:
        cur.execute("INSERT INTO Person (NID, Pname, Phone_no, Email, DOB, Gender, Ppassword) VALUES (%s, %s, %s, %s, %s, %s, %s)", (NID, full_name, phone_no, email, DOB, gender, password))
        cur.execute("INSERT INTO User (NID) VALUES (%s)", (NID,))
        db_conn.commit()
    cur.close()

