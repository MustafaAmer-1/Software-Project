from . import storage_wrapper

db_conn = storage_wrapper.db_conn

def get_all_trips():
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Trip")
    trips = cur.fetchall()
    cur.close()
    return trips

def get_trips(source, distnation, departure_date, from_time, to_time):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Trip WHERE sourceStation=%s AND destinationStation=%s AND DepartureDate=%s AND DepartureTime BETWEEN %s AND %s", 
                (source, distnation, departure_date, from_time, to_time))
    trips = cur.fetchall()
    cur.close()
    return trips

def delete_trip(tripID):
    cur = db_conn.cursor()
    cur.execute('delete from Trip where TripID=%s' , (tripID , ))
    db_conn.commit()
    cur.close()

def get_booked_seats(tripID):
    cur = db_conn.cursor()
    cur.execute('SELECT SeatID FROM Seat WHERE TripID=%s' , (tripID , ))
    seats = cur.fetchall()
    cur.close()
    return seats

def get_schedule():
    cur = db_conn.cursor()
    cur.execute("SELECT T.TripID, T.DepartureDate, S1.Sname, S2.Sname, T.DepartureTime, T.ArrivalTime FROM Trip T, Station S1, Station S2 WHERE (T.StationID=S1.StationID AND T.TOStationID=S2.StationID)")
    trips = cur.fetchall()
    cur.close()
    return trips