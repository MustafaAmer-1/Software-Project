from . import storage_wrapper

db_conn = storage_wrapper.db_conn

# TODO: insert into db after getting user data
def reserve_ticket(tripID, seatID):
    pass

def get_all_tickets():
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Ticket")
    tickets = cur.fetchall()
    cur.close()
    return tickets

def delete_ticket(ticketID):
    cur = db_conn.cursor()
    cur.execute("DELETE FROM Ticket WHERE Ticket_ID = %s", (ticketID,))
    db_conn.commit()
    cur.close()
    
def get_ticket_data(ticketID):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Ticket WHERE Ticket_ID = %s", (ticketID,))
    ticket_data = cur.fetchone()
    cur.close()
    return ticket_data

def get_ticket_by_id(ticketID):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Ticket WHERE Ticket_ID = %s", (ticketID,))
    ticket = cur.fetchone()
    cur.close()
    return ticket
