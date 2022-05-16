import sys, os

from app.services.trip_service import add_trip, delete_trip
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from flask import render_template, session , request, Blueprint , redirect

from services import trip_service

trip_manage = Blueprint('trip_manage', __name__)

@trip_manage.route("/add_trip" , methods = ['GET' ,'POST'])
def add_trip():
    if request.method == 'POST':
        if not session.get("id"):
            return redirect("/login")
        else:    
            DepartureTime = request.form.get('DepartureTime')
            DepartureDate = request.form.get('DepartureDate')
            ArrivalTime = request.form.get('ArrivalTime')
            TripID = request.form.get('TripID')
            StationID = request.form.get('StationID')
            TOStationID = request.form.get('TOStationID')
            trip_service.add_trip(DepartureTime , DepartureDate , ArrivalTime , TripID , StationID , TOStationID)
    return render_template("addTrip.html")






@trip_manage.route('/delete_trip/<TripID>' , methods = ['GET' , 'POST'])
def delete_trip(TripID):
    if request.method == 'POST':
        delete_trip(TripID)
        trips = trip_service.get_all_trips()
    return render_template("edittrain.html" , trips = trips)