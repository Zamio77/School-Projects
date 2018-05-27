"""
Creation of the CAR class for use in
file LamarDougM09_Ch10Ex2_MAIN. This is
the class that is being referenced.
"""

class Car:

    # Initiate the class
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Start the accelerate function
    def accelerate(self):
        self.__speed += 5

    # Start the brake function
    def brake(self):
        self.__speed -= 5

    # Start the get_speed function
    def get_speed(self):
        return self.__speed


    
