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
    cur.execute("SELECT * FROM Trip WHERE StationID=%s AND TOStationID=%s AND DepartureDate=%s AND DepartureTime BETWEEN %s AND %s", 
                (source, distnation, departure_date, from_time, to_time))
    trips = cur.fetchall()
    cur.close()
    return trips

def get_trip(tripID):
    cur = db_conn.cursor()
    cur.execute('SELECT * FROM Trip WHERE TripID=%s' , (tripID , ))
    trip = cur.fetchone()
    cur.close()
    return trip

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

def get_trips_rows():
    trips = get_all_trips()
    for i in range(len(trips)):
        bkSeats = get_booked_seats(trips[i][0])
        strSeats = " ".join(str(trips[i][0]) + "-" + str(x[0]) for x in bkSeats)
        trips[i] = list(trips[i])
        trips[i].append(strSeats)
    return trips

def get_schedule():
    cur = db_conn.cursor()
    cur.execute("SELECT T.TripID, T.DepartureDate, S1.Sname, S2.Sname, T.DepartureTime, T.ArrivalTime FROM Trip T, Station S1, Station S2 WHERE (T.StationID=S1.StationID AND T.TOStationID=S2.StationID)")
    trips = cur.fetchall()
    cur.close()
    return trips
