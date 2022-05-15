from person import Person

from datetime import datetime

class User(Person):
    def __init__(self, name, NID, email):
        super().__init__(name, NID, email)
    
    def getComingTicket(self):
        comingTicket = self.__tickets[0]
        min_diff = self.__tickets[0].reservationDate - datetime.now()
        for ticket in self.__tickets:
            if ticket.reservationDate > datetime.now()  and ticket.reservationDate - datetime.now() < min_diff:
                comingTicket = ticket
        return comingTicket
    
    def getComingTickets(self):
        comingTickets = []
        for ticket in self.__tickets:
            if ticket.reservationDate > datetime.now():
                comingTickets.append(ticket)
        return comingTickets
