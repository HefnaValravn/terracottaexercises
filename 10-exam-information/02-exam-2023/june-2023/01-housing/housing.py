from abc import ABC, abstractmethod

class Person:
    def __init__(self, id, name, is_a_student):
        self.id = id
        self.is_a_student = is_a_student
        self.__name = name
        
        
    @staticmethod
    def is_valid_name(name):
        test = name.split(' ')
        if len(test) > 1:
            return True
        else:
            return False
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def setname(self, name):
        if Person.is_valid_name(name):
            self.__name = name
        else:
            raise ValueError
            
            
            


@ABC
class Residence:
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}
        
    
    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    
    
    @property
    def maximum_occupants(self):
        return self.area // len(self.__occupants)
    
    
    def register_resident(self, person):
        if (len(self.__occupants) * 20) > (self.area - 20):
            raise RuntimeError
        else:
            self.__occupants[person.id] = person
            
            
    def unregister_resident(self, id):
        del self.__occupants[id]
        
    @property
    def resident_names(self):
        toReturn = []
        for value in self.__occupants.items():
            toReturn.append(value.name)
        return toReturn
    
    @abstractmethod
    def calculate_value(self):
        ...
    
    
    
    
class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity
        self.__occupants = {}
        
        
    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (1000 * self.garage_capacity)
    
    
    def register_resident(self, person):
        if (len(self.__occupants) * 20) > (self.area - 20):
            raise RuntimeError
        else:
            self.__occupants[person.id] = person
    
    
class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address, area)
        self.number_of_rooms = 1
        self.__occupants = {}
        
        
    def register_resident(self, person):
        if not person.is_a_student:
            raise RuntimeError
        else:
            self.__occupants[person.id] = person
            
    
    def calculate_value(self):
        return 150000 + (750 * self.area)