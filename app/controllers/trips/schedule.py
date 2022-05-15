import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from services import trip_service

from flask import render_template, flash, redirect, url_for, request, Blueprint

schedule_manage = Blueprint('schedule_manage', __name__)

@schedule_manage.route('/schedule', methods=['GET', 'POST'])
def schedule():
    trips = trip_service.get_schedule()
    return render_template('schedule.html', trips=trips)