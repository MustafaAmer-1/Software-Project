from . import storage_wrapper

db_conn = storage_wrapper.db_conn

def get_available_stations():
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Station")
    stations = cur.fetchall()
    cur.close()
    return stations

def get_station_name(stationID):
    cur = db_conn.cursor()
    cur.execute("SELECT Sname FROM Station WHERE StationID = %s", (stationID,))
    station = cur.fetchone()[0]
    cur.close()
    return station
