from . import storage_wrapper
from flask import session
from datetime import datetime

db_conn = storage_wrapper.db_conn

def reserve_ticket(tripID, seatID):
    cur = db_conn.cursor()
    NID = session['id']
    cur.execute("INSERT INTO Ticket (Price, TDate, TripID, Owner_NID) VALUES (%s, %s, %s, %s)", (250, datetime.now(), tripID, NID))
    cur.execute("INSERT INTO Seat (SeatID, CarNo, TripID, Ticket_ID) VALUES (%s, %s, %s, %s)", (seatID, 10, tripID, cur.lastrowid))
    db_conn.commit()
    cur.close()

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
    
def get_ticket(ticketID):
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



def sum_tickets_by_month(year=2022):
    query = """
        SELECT MONTH(TDate), SUM(Price)
        FROM Ticket
        WHERE YEAR(TDate) >= %s 
        GROUP BY MONTH(TDate)
    """
    revenue_per_month = [0 for _ in range(12)]
    
    cursor = db_conn.cursor()
    cursor.execute(query, [year])
    accum_tickets = cursor.fetchall()
    cursor.close()
    return accum_tickets