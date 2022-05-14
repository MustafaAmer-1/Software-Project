from flask import Flask

from app.controllers.tickets.reserve_ticket import reserve_ticket

APP = Flask(__name__)
APP.register_blueprint(reserve_ticket)

if __name__ == "__main__":
    APP.run(debug=True)