import sys, os

from app.services.login_service import choose_type, get_credientials
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from flask import  session , redirect, Blueprint

logout_manage = Blueprint('logout_manage', __name__)

@logout_manage.route('/logout')
def logout():
    session.pop('loggedin' , None)
    session.pop('id' , None)
    return redirect('/login')