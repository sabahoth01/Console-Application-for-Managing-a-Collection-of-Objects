class House:
    def __init__(self, name=None, year=None, number_of_floors=None, number_of_flats_on_floor=None, number_of_lifts=None):
        self.name = name  # Can be null

        if year <=0 or year > 639:
            raise ValueError("Year must be between 1 and 639")
        else:
            self.year = year  # Maximum value: 639, must be greater than 0
        if number_of_floors <=0 :
            raise ValueError("Number of floors must be greater than 0!!")
        else:
            self.number_of_floors = number_of_floors  # Must be greater than 0
        if number_of_flats_on_floor <=0 :
            raise ValueError("Number of flats of floors must be greater than 0!!")
        else:
            self.number_of_flats_on_floor = number_of_flats_on_floor  # Must be greater than 0
        if number_of_lifts <=0 :
            raise ValueError("Number of lifts must be greater than 0!!")
        else:
            self.number_of_lifts = number_of_lifts  # Must be greater than 0