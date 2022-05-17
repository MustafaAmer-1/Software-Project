import sys, os

from app.services.login_service import choose_type, get_credientials
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from flask import render_template, session , request, Blueprint , redirect

from services import login_service

login_manage = Blueprint('login_manage', __name__)

@login_manage.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')
        record = get_credientials(username)
        if record:
            if (record and password == record[6]):
                type = choose_type(record[0])
                if (type == 1):
                    session['id'] = record[1]
                    session['loggedin'] = True
                    return redirect('/homepageadm')
                elif(type == 2):
                    session['id'] = record[1]
                    session['loggedin'] = True
                    return redirect('/homepageclerk')
                
            else:
                error = "Invalid Password Please Try again"
        
    return render_template('login.html' , error = error)