import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from services import trip_service, ticket_service, stations_service

from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)

reserve_ticket = Blueprint('reserve_ticket', __name__)

@reserve_ticket.route('/reserve_ticket', methods=['GET'])
def view_trips():
    trips_rows = trip_service.get_trips_rows()
    stations = stations_service.get_available_stations()
    return render_template('resrveTicket.html', trips=trips_rows, stations=stations)

@reserve_ticket.route('/reserve_ticket', methods=['POST'])
def search_trip():
    form = request.form
    source = form['source']
    distnation = form['distnation']
    departure_date = form['departure_date']
    from_time = form['from_time']
    to_time = form['to_time']
    trips = trip_service.get_trips(source, distnation, departure_date, from_time, to_time)
    return render_template('resrveTicket.html', trips=trips)

@reserve_ticket.route('/reserve', methods=['POST'])
def reserve():
    tripID, seatID = request.form['seat'].split('-')
    ticket_service.reserve_ticket(tripID, seatID)
    return redirect('/')
    