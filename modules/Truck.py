"""
Truck.py
~

Western Governors University
C950: Data Structures & Algorithms II

~

Kevin Salazar
Student ID: 010303855

~

December 21st 2023

"""
# Initializing truck object attributes.
class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    # Returning a string representation of truck object.
    def __str__(self):
        return (f"Capacity: {self.capacity} | Speed: {self.speed} | Load: {self.load} | "
                f"Packages: {self.packages} | Mileage: {self.mileage} | Address: {self.address} | "
                f"Departure Time: {self.depart_time}")