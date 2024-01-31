"""
Package.py
~

Western Governors University
C950: Data Structures & Algorithms II

~

Kevin Salazar
Student ID: 010303855

~

December 21st 2023

"""
import datetime

class Package:
    # Initializing the package object attributes.
    def __init__(self, ID, address, city, state, zipcode, deadlineTime, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadlineTime = deadlineTime
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    # Returns a String representation of the Package object
    def __str__(self):
        return f"ID: {self.ID} | {self.address} {self.city} {self.state}, {self.zipcode} | Deadline: {self.deadlineTime} | Weight: {self.weight} | Delivery time: {self.delivery_time} | Status: {self.status}"

# # call this function instead
#     # todo Dont show delivery time, just a plain status. Delivered or not.
#     def print_status(self,inputTime):
#         new_address = self.address
#         if self.ID == 9:
#             if inputTime < datetime.timedelta(hours=10, minutes=20):
#                 new_address = "300 State St"
#             else:
#                 new_address = "410 S State S"
#
#         return f"ID: {self.ID} | {new_address} {self.city} {self.state}, {self.zipcode} | Deadline: {self.deadlineTime} | Weight: {self.weight} | Delivery time: {self.delivery_time} | Status: {self.status}"


    # Updates the status of the package based on the departure and delivery time.
    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.status = "Package has been delivered."
        elif self.departure_time > convert_timedelta:
            self.status = "Package in transit."
        else:
            self.status = "Package at hub."

        self.update_special_case(convert_timedelta)

    # Handling the special case for package with ID 9.
    #
    def update_special_case(self, convert_timedelta):
        if self.ID == 9:
            if convert_timedelta > datetime.timedelta(hours=10, minutes=20, seconds=0):
                self.address = "410 S State St"
                self.zipcode = "84111"
            else:
                self.address = "300 State St"
                self.zipcode = "84103"
