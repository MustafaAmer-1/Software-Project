import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from services import employee_service, stations_service

from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)

employee_manage = Blueprint('employee_manage', __name__)

@employee_manage.route("/add_clerk" , methods = ['GET' ,'POST'])
def add_clerk():
    if request.method == 'POST':
        clerkName = request.form.get('clerk name')
        NID = request.form.get('NID')
        BD = request.form.get('BD')
        Email = request.form.get('Email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        Gender = request.form.get('Gender')
        station = request.form.get('station')
        start_time = request.form.get('start')
        end_time = request.form.get('end')
        employee_service.add_clerk(NID, clerkName, phone, Email, BD, Gender, password, station, start_time, end_time)
    stations = stations_service.get_available_stations()
    return render_template("addClerk.html", stations=stations)
