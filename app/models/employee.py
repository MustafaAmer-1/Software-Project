from person import Person

from datetime import datetime
    
class Employee(Person):
    def __init__(self, name, NID, email):
        super().__init__(name, NID, email)
        
        