import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from time import strftime, gmtime

from services import ticket_service
from services import stations_service
from services import trip_service


from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)

edit_ticket = Blueprint('edit_ticket', __name__)


@edit_ticket.route('/edit_ticket', methods=['POST'])
def edit():
    ticketID = request.form['ticketID']
    ticket = ticket_service.get_ticket(ticketID)
    ticket_data = {}
    trip = trip_service.get_trip(ticket[3])
    ticket_data['source'] = trip[4]
    ticket_data['dist'] = trip[5]
    ticket_data['date'] = trip[1]
    ticket_data['from'] = strftime("%H:%M", gmtime(trip[2].seconds))
    ticket_data['to'] = strftime("%H:%M", gmtime(trip[2].seconds))
    stations = stations_service.get_available_stations()
    return render_template('edit_ticket.html', ticket_data=ticket_data, stations=stations)
