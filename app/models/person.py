class Person:
    def __init__(self, name, NID, email):
        self.__name = name
        self.__NID = NID
        self.__email = email
        self.__tickets = []

    def add_ticket(self, ticket):
        self.__tickets.append(ticket)

    def __str__(self):
        return f"{self.__name} - {self.__NID} - {self.__email}"
