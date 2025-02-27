class House:
    def __init__(self, name=None, year=None, number_of_floors=None, number_of_flats_on_floor=None, number_of_lifts=None):
        self.name = name  # Can be null
        self.year = year  # Maximum value: 639, must be greater than 0
        self.number_of_floors = number_of_floors  # Must be greater than 0
        self.number_of_flats_on_floor = number_of_flats_on_floor  # Must be greater than 0
        self.number_of_lifts = number_of_lifts  # Must be greater than 0