"""
Main.py
~

Western Governors University
C950: Data Structures & Algorithms II

~

Kevin Salazar
Student ID: 010303855

~

December 21st 2023

"""

import csv
import datetime
import Truck
import time
from builtins import ValueError
from HashTableCreation import HashMapCreation
from Package import Package

# Opening the CSV files and loading the data contained in them.
with open("CSV_files/Distance.csv") as csvfile1:
    CSV_Distance = csv.reader(csvfile1)
    CSV_Distance = list(CSV_Distance)

with open("CSV_files/Address.csv") as csvfile2:
    CSV_Address = csv.reader(csvfile2)
    CSV_Address = list(CSV_Address)

with open("CSV_files/Package.csv") as csvfile3:
    CSV_Package = csv.reader(csvfile3)
    CSV_Package = list(CSV_Package)


# The following function loads package data into the hash table
def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            # Extracting package information from CSV
            p_ID = int(package[0])
            p_Address = package[1]
            p_City = package[2]
            p_State = package[3]
            p_zipCode = package[4]
            p_deadlineTime = package[5]
            p_Weight = package[6]
            p_Status = "In transit, delivery time displayed is expected delivery time."

            # Package object gets created and inserted into the hash table
            p = Package(p_ID, p_Address, p_City, p_State, p_zipCode, p_deadlineTime, p_Weight, p_Status)
            package_hash_table.insert(p_ID, p)


# The following function calculates the distance between two points
def distance_in_between(x_value, y_value):
    distance = CSV_Distance[x_value][y_value]
    if distance == '':
        distance = CSV_Distance[y_value][x_value]

    return float(distance)


# The following function is used to extract the address information from the CSV files
def extract_address(address):
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])


# Creating Truck objects with the specified package assignments
truck1 = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

truck2 = Truck.Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck3 = Truck.Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))

# Creating a hash map for package storage
storage_package_hash = HashMapCreation()

# Loading package data into the hash table
load_package_data("CSV_files/Package.csv", storage_package_hash)


# Function to simulate delivering packages for a truck
# This function uses the Nearest Neighbor Algorithm
# Using the distances that the truck drives once a package has been sorted
def delivering_packages(truck):
    # Placing packages into an array called 'not_yet_delivered', this is the path
    not_yet_delivered = []

    # Iterating through package ID in truck.packages list
    for packageID in truck.packages:
        # Looking up the package ID on the storage hash table
        package = storage_package_hash.lookup(packageID)
        # Appends package to 'not yet delivered' list.
        not_yet_delivered.append(package)
        # Clear the package list of a given truck
        # This way the packages can be placed back in order of the nearest neighbor
    truck.packages.clear()

    # Delivery loop that continues until the 'not yet delivered' list is empty.
    # Adds the nearest package into the truck.packages list one by one
    # Finds the closest undelivered package to the truck
    while len(not_yet_delivered) > 0:
        next_address = 2000
        next_package = None
        # Iterating through packages in 'not yet delivered' list
        for package in not_yet_delivered:
            # It calculates the distance between the current location of the truck and the delivery address of each
            # package using the distance_in_between function.
            if distance_in_between(extract_address(truck.address), extract_address(package.address)) <= next_address:
                # If the distance calculated for the current package is less than or equal to the current
                # next_address, it updates the next_address variable with this smaller distance.
                next_address = distance_in_between(extract_address(truck.address), extract_address(package.address))
                next_package = package
        # Adding the closest 'next package' to 'truck package' list
        truck.packages.append(next_package.ID)
        # Removing the same 'next package' from 'not yet delivered list'
        not_yet_delivered.remove(next_package)
        # Increments the truck's mileage by adding the distance 'next_address' traveled for delivering this package.
        truck.mileage += next_address
        # Updates the truck's current address to the address of the next_package.
        truck.address = next_package.address
        # Updates the truck's current time by adding the time taken to travel the next_address distance at a given
        # speed (here, 18 units per hour).
        truck.time += datetime.timedelta(hours=next_address / 18)
        # Sets the delivery_time attribute of the next_package to the current time of the truck.
        # Marks the time when the package is delivered.
        next_package.delivery_time = truck.time
        # Sets the departure_time attribute of the next_package to the departure time of the truck.
        # Presumably used for tracking the time the truck left with the package for delivery.
        next_package.departure_time = truck.depart_time


# Simulating package deliveries for each truck
delivering_packages(truck1)
delivering_packages(truck2)
# Calculates the departure time for truck3 based on the minimum time between truck1 and truck2.
# The min function determines the smallest time between truck1.time and truck2.time.
truck3.depart_time = min(truck1.time, truck2.time)
delivering_packages(truck3)


# The Main class, which interacts with the user
class Main:
    print("================================================================")
    print("==== Welcome to Western Governors University Parcel Service ====")
    print("================================================================")
    # Printing the mileage for trucks and route
    print("The separate mileage for trucks 1, 2 and 3 are the next:")

    print("Truck 1 = " + str(truck1.mileage))
    print("Truck 2 = " + str(truck2.mileage))
    print("Truck 3 = " + str(truck3.mileage))

    print("The total mileage for the proposed route is: " + str(
        truck1.mileage + truck2.mileage + truck3.mileage) + " miles.")

    # Getting user input for the time to check package statuses
    userTime = input("Enter a time to generate a report for package status."
                     " Using the standard HH:MM:SS format.\n")
    (hr, mn, sc) = userTime.split(":")
    convertTimeDelta = datetime.timedelta(hours=int(hr), minutes=int(mn), seconds=int(sc))

    while True:
        # Checking user input for package status or exit
        initialInput = input("To check the status of your package, please type 'status'."
                             "  To exit, type 'exit'.\n")
        if initialInput == "status":
            break

        elif initialInput == "exit":
            exit()
        else:
            print("You have entered: " + initialInput + ".  Type 'status' to check the status of your package, "
                                                        "or 'exit' to exit.")

    print("====================================================================")
    print("To display the status of all packages, type 'list'.")
    print("To display the status of an individual package, type 'individual'.")
    print("====================================================================")
    time.sleep(.3)

    while True:
        # Getting user input for package list, individual package, or exit
        followingInput = input("To exit, type 'exit'.")
        if followingInput == "list":
            time.sleep(1.2)
            while True:
                # Looping through all packages to display their statuses
                try:
                    for packageID in range(1, 41):
                        package = storage_package_hash.lookup(packageID)
                        package.update_status(convertTimeDelta)
                        time.sleep(.10)
                        print(str(package))
                    print("\nTo check a different package, "
                          "program needs to be rerun.\n")
                    break
                except ValueError:
                    continue

        elif followingInput == "individual":
            while True:
                try:
                    # Getting user input for individual package ID
                    packageNum = int(input("Enter the package ID number:\n"))
                    if packageNum > 0 and packageNum <= 40:
                        package = storage_package_hash.lookup(int(packageNum))
                        package.update_status(convertTimeDelta)
                        time.sleep(.10)
                        print(str(package))
                        break
                    else:
                        print("Invalid input, you entered: " + str(packageNum) + ". Enter a valid package number.")
                        continue

                except ValueError:
                    continue
            break
        elif followingInput == "exit":
            exit()
        else:
            print("You entered: " + followingInput + ".  Type 'list' to display a list of the status of all "
                                                     "packages, type 'individual' to check the status"
                                                     "of an individual package, type 'exit' to exit.")
    print("To check an additional package, program needs to be rerun.")


exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
