import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from services import ticket_service

from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)

ticket_manage = Blueprint('ticket_manage', __name__)

@ticket_manage.route('/ticket_manage', methods=['GET'])
def view_tickets():
    tickets = ticket_service.get_all_tickets()
    return render_template('ticket_manage.html', tickets=tickets)

@ticket_manage.route('/ticket_manage', methods=['POST'])
def search_tickets():
    Ticket_ID = request.form['Ticket_ID']
    ticket = ticket_service.get_ticket_by_id(Ticket_ID)
    if(ticket == None): 
        return render_template('ticket_manage.html') 
    return render_template('ticket_manage.html', tickets=[ticket])
    
@ticket_manage.route('/delete_ticket', methods=['POST'])
def delete_ticket():
    ticketID = request.form['ticketID']
    ticket_service.delete_ticket(ticketID)
    return redirect('/ticket_manage')
