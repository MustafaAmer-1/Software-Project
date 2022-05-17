import sys, os

from app.services.login_service import choose_type, get_credientials
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from flask import render_template, session , Blueprint , redirect


manage_dashboard = Blueprint('manage_dashboard', __name__)

@manage_dashboard.route('/homepageadm')
def homepageadm():
    if not session.get("id"):
        return redirect("/login")
    return render_template('ManagerDashboard.html' , username = session["id"])


@manage_dashboard.route('/homepageuser')
def homepageuser():
    if not session.get("id"):
        return redirect("/login")
    return render_template('UserDashboard.html' , username = session["id"])


@manage_dashboard.route('/homepageclerk')
def homepageclerk():
    if not session.get("id"):
        return redirect("/login")
    return render_template('ClerkDashboard.html' , username = session["id"])