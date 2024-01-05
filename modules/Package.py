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
# Class for package object creation, named Package
class Package:
    def __init__(self, ID, address, city, state, zipcode, deadlineTime, weight, status):
        # Initializing package attributes
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

    def __str__(self):
        # Representation in String for the Package object
        '''return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.deadlineTime, self.weight, self.delivery_time,
                                                       self.status)'''
        return "ID: %s  | %s %s %s, %s | Deadline: %s | Weight: %s | Delivery time: %s | Status: %s" % (self.ID, self.address, self.city, self.state, self.zipcode, self.deadlineTime,
        self.weight, self.delivery_time, self.status)

    def update_status(self, convert_timedelta):
        # Updates the status of package, depending on its delivery and departure times
        if self.delivery_time < convert_timedelta:
            self.status = "Delivered"
        elif self.departure_time > convert_timedelta:
            self.status = "In transit, expected delivery time is displayed."
        else:
            self.status = "At hub, expected delivery time is displayed."
        if self.ID == 9:
                if convert_timedelta > datetime.timedelta(hours=10, minutes=20, seconds=00):
                    self.address = "410 S State St"
                    self.zipcode = "84111"
                else:
                    self.address = "300 State St"
                    self.zipcode = "84103"
