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
                session['id'] = record[0]
                session['loggedin'] = True
                if (type == 1):
                    return redirect('/homepageadm')
                elif(type == 2):
                    return redirect('/homepageclerk')
                elif(type == 3):
                    return redirect('/homepageuser')
                
            else:
                error = "Invalid Password Please Try again"
        
    return render_template('login.html' , error = error)