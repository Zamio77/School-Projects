"""
This program uses the car class
to add and remove to the speed of
the car.
"""

import LamarDougM02_Ch10Ex2_CAR

def main():

    year_model = "2005 Toyota"
    make = "Matrix"

    entry = LamarDougM02_Ch10Ex2_CAR.Car(year_model, make)

    for i in range(1, 6):
        entry.accelerate()
        print("Speed:", entry.get_speed())

    for i in range(1, 6):
        entry.brake()
        print("Speed:", entry.get_speed())


main()
