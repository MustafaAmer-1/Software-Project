from . import storage_wrapper

db_conn = storage_wrapper.db_conn

def get_user_history(user_id):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Ticket WHERE Owner_NID = %s", (user_id,))
    tickets = cur.fetchall()
    for i in range(len(tickets)):
        tickets[i] = list(tickets[i])
        cur.execute("SELECT SeatID FROM Seat WHERE Ticket_ID = %s", (tickets[i][0],))
        tickets[i].append(cur.fetchone()[0])
    return tickets
