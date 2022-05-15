from abc import ABC, abstractmethod
from datetime import datetime

class Ticket(ABC):
    @abstractmethod
    def __init__(self, trip, id, seat, passengerName, passengerSSN, source, distnaton, price):
        self.__trip = trip
        self.__id = id
        self.__seat = seat
        self.__passengerName = passengerName
        self.__passengerSSN = passengerSSN
        self.__source = source 
        self.__distnaton = distnaton 
        self.__price = price
        self.__reservationDate = datetime.now()
    
                
class ElectronicTicket(Ticket):
    def __init__(self, trip, id, seat, passengerName, passengerSSN, source, distnaton, price, owner):
        super().__init__(trip, id, seat, passengerName, passengerSSN, source, distnaton, price)
        self.__owner = owner

class PaperTicket(Ticket):
    def __init__(self, trip, id, seat, passengerName, passengerSSN, source, distnaton, price, initiator):
        super().__init__(trip, id, seat, passengerName, passengerSSN, source, distnaton, price)
        self.__initiator = initiator
