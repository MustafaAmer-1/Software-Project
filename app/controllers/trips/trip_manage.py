import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from services import trip_service

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session
)

trip_manage = Blueprint('trip_manage', __name__)

@trip_manage.route('/trip_manage', methods=['GET'])
def view_trips():
    trips = trip_service.get_all_trips()
    return render_template('trip_manage.html', trips=trips, username = session['id'])

@trip_manage.route('/delete_trip/<TripID>' , methods = ['POST'])
def delete_trip(TripID):
    trip_service.delete_trip(TripID)
    return redirect('/trip_manage')
