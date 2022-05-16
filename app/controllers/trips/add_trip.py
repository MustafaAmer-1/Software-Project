import sys, os

from app.services.trip_service import add_trip
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from flask import render_template, session , request, Blueprint , redirect

from services import trip_service

add_trip_manage = Blueprint('add_trip_manage', __name__)

@add_trip_manage.route("/add_trip" , methods = ['GET' ,'POST'])
def add_trip_view():
    if request.method == 'POST':
        if not session.get("username"):
            return redirect("/login")
        else:    
            DepartureTime = request.form.get('DepartureTime')
            DepartureDate = request.form.get('DepartureDate')
            ArrivalTime = request.form.get('ArrivalTime')
            TripID = request.form.get('TripID')
            StationID = request.form.get('StationID')
            TOStationID = request.form.get('TOStationID')
            add_trip(DepartureTime , DepartureDate , ArrivalTime , TripID , StationID , TOStationID)
    return render_template("addTrip.html")