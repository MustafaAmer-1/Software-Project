from datetime import datetime

from station import Station

# TODO: getAvailableSeats && bookSeat
class Trip():
    def __init__(self, tripID:int, trainID:int, source:Station, distination:Station, depatureTime:str):
        self.__tripID = tripID
        self.__trainID = trainID
        self.__source = source
        self.__distination = distination
        self.__depatureTime = datetime.strptime(depatureTime)
