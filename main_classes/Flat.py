from datetime import datetime
from datetime import datetime

class Flat:
    _id_counter = 0
    def __init__(self, name, coordinates, area, number_of_rooms, floor, central_heating, transport, house=None):
        Flat._id_counter += 1
        self.id = Flat._id_counter  # Must be greater than 0, unique, and generated automatically
        if name == '' or None:
            raise ValueError('Name is required and Cannot be null or empty!!')
        else:
            self.name = name  # Cannot be null or empty
        if coordinates == '' or None:
            raise ValueError('Coordinates are required and Cannot be null or empty!!')
        else:
            self.coordinates = coordinates  # Cannot be null
            self.creation_date = self.generate_creation_date()  # Cannot be null, generated automatically
        if area <= 0:
            raise ValueError('area must be greater than 0!!')
        else:    
            self.area = area  # Must be greater than 0
        if number_of_rooms <= 0:
            raise ValueError('Name must be greater than 0!!')
        else:
            self.number_of_rooms = number_of_rooms  # Must be greater than 0
        if floor <= 0:
            raise ValueError('Floor must be greater than 0!!')
        else:
            self.floor = floor  # Must be greater than 0
        if central_heating is None:
            raise ValueError('Central heating is required and Cannot be null!!')
        else:
            self.central_heating = central_heating  # Cannot be null
        if transport == '' or None:
            raise ValueError('Transport is required and Cannot be null or empty!!')
        else:
            self.transport = transport  # Cannot be null
       
        self.house = house  # Can be null

    def generate_creation_date(self):
        return datetime.now()

# # Example usage
# flat1 = Flat("Flat A", (10.0, 20), 50.0, 2, 3, True, "NONE")

# print(f"Flat 1 ID: {flat1.id}")
# print(f"Flat 2 ID: {flat2.id}")
# print(flat1)