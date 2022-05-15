import sys, os

from app.services.login_service import choose_type, get_credientials
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from flask import render_template, session , request, Blueprint

from services import login_service

login_manage = Blueprint('login_manage', __name__)

@login_manage.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')
        record = get_credientials(username , password)
        if record:
            type = choose_type(record[0])
            if (type == 1):
                session['username'] = record[1]
                session['loggedin'] = True
                return render_template('ManagerDashboard.html' , username = record[1])


            

            
        else:
            error = "Invalid Email/Password Please Try again"
    return render_template('login.html' , error = error)