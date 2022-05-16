import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from services import history_service

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session
)

history = Blueprint('history', __name__)

@history.route('/history', methods=['GET'])
def view_history():
    history_rows = history_service.get_user_history(session['id'])
    return render_template('history.html', history_rows=history_rows)
