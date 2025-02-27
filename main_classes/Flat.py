from datetime import datetime
import random

class Flat:
    _id_counter = 0
    def __init__(self, name, coordinates, area, number_of_rooms, floor, central_heating, transport, house=None):
        Flat._id_counter += 1
        self.id = Flat._id_counter  # Must be greater than 0, unique, and generated automatically
        self.name = name  # Cannot be null or empty
        self.coordinates = coordinates  # Cannot be null
        self.creation_date = self.generate_creation_date()  # Cannot be null, generated automatically
        self.area = area  # Must be greater than 0
        self.number_of_rooms = number_of_rooms  # Must be greater than 0
        self.floor = floor  # Must be greater than 0
        self.central_heating = central_heating  # Cannot be null
        self.transport = transport  # Cannot be null
        self.house = house  # Can be null

    def generate_creation_date(self):
        from datetime import datetime
        return datetime.now()

# # Example usage
# flat1 = Flat("Flat A", (10.0, 20), 50.0, 2, 3, True, "NONE")

# print(f"Flat 1 ID: {flat1.id}")
# print(f"Flat 2 ID: {flat2.id}")
# print(flat1)