from flask import Flask

from app.controllers.tickets.reserve_ticket import reserve_ticket

from app.controllers.Session.register import register_manage

from app.controllers.tickets.ticket_manage import ticket_manage

from app.controllers.trips.schedule import schedule_manage

APP = Flask(__name__)
APP.secret_key = 'secret'
APP.register_blueprint(reserve_ticket)
APP.register_blueprint(register_manage)
APP.register_blueprint(ticket_manage)
APP.register_blueprint(schedule_manage)

if __name__ == "__main__":
    APP.run(debug=True)