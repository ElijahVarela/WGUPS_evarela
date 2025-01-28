# Student: Elijah Varela
# Student ID: 010892662
# Title: WGUPS Project

from HashTable import HashTable
from Package import Package
from Truck import Truck
import csv
from datetime import timedelta

# Defines the truck speed in miles per minute for time calculations.
truck_speed = 18/60
# Function to load package data from a CSV file into a hash table.
# Time Complexity: O(n)
def load_package_data(package_file, hash_table):
    # Opens the CSV file containing package information.
    with open(package_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Iterates over each row in the CSV file.
        for row in csv_reader:
            # Extracts and formats package data from the CSV columns.
            package_id = int(str.strip(row[0]))
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            notes = row[7]
            # Creates a package object with the extracted data.
            packages_hashed = Package(package_id, address, city, state, zip_code, deadline, weight, notes)
            # Inserts the package object into the hash table.
            hash_table.insert(package_id, packages_hashed)
    # Returns the updated hash table containing package data.
    return hash_table

# Function to load address data from a CSV file.
def load_distance_data(file_name):
    # Initializes a list to store the distance data.
    distance_data = []
    # Opens the CSV file containing distance information.
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Iterates over each row in the CSV file.
        for row in csv_reader:
            # Converts distance values to float and handles empty cells.
            distance_data.append([float(x) if x else 0.0 for x in row])
    # Returns the distance matrix data.
    return distance_data

# Function to load address data from a CSV file.
def load_address_data(file_name):
    # Initializes a list to store the address data.
    address_data = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # Extract and standardize addresses from column 2 (index 2).
            address_data.append(str.strip(row[2]))
    # Returns the list of addresses.
    return address_data

# Function to calculate the distance between two addresses.
def distance_between(address1, address2, address_data, distance_data):
    # Checks if both addresses are valid.
    if address1 not in address_data or address2 not in address_data:
        # Prints an error message if either address is invalid.
        print('One or both locations are invalid')
        return
    else:
        # Retrieves matrix indices for both addresses.
        i = address_data.index(address1)
        j = address_data.index(address2)
        # Returns the distance based on the indices.
        if i > j:
            return distance_data[i][j]
        else:
            return distance_data[j][i]

# Function to update the information for package 9.
def update_package_9(convert_timedelta):
    # Checks if the time is after 10:20 AM.
    if convert_timedelta >= timedelta(hours = 10, minutes = 20, seconds = 0):
        # Updates package 9 with the corrected address and details.
        updated_package_9 = Package(
            package_id=9,
            address="410 S State St",  # Corrected address
            city="Salt Lake City",
            state="UT",
            zip_code="84111",
            deadline="EOD",
            weight="2",
            notes="Address was updated at 10:20am",
        )
        # Inserts the updated package into the hash table.
        new_table.insert(9, updated_package_9)
        # Initiates package delivery for truck three.
        truck_three.deliver_packages(new_table, loaded_address_data, loaded_distance_data)
    else:
        # Keeps the initial address and details for package 9.
        updated_package_9 = Package(
            package_id=9,
            address="300 State St",  # Corrected address
            city="Salt Lake City",
            state="UT",
            zip_code="84103",
            deadline="EOD",
            weight="2",
            notes="Wrong address listed",
        )
        # Inserts the package into the hash table.
        new_table.insert(9, updated_package_9)
        # Initiates package delivery for truck three.
        truck_three.deliver_packages(new_table, loaded_address_data, loaded_distance_data)

# Function to print detailed information about a package.
def print_information(package):
    # Display all relevant details of a package in a formatted output.
    print(f"[Package ID: {package.package_id}] "
        f"[Status: {package.status}] "
        f"[Delivery Time: {package.delivery_time}] "
        f"[Deadline: {package.deadline}] "
        f"[Address: {package.address}, "
        f"City: {package.city}, "
        f"State: {package.state}, "
        f"Zipcode: {package.zip_code}] "
        f"[Weight: {package.weight}] "
        f"[Notes: {package.notes}]")
    print("-" * 250) # Separator for better readability.


# Function to print all delivered packages and the total mileage of all trucks.
def print_all_delivered_packages(print_all_new_table, print_truck_one, print_truck_two, print_truck_three):
    # Update package #9's status based on truck three's departure ti1
    # me.
    update_package_9(print_truck_three.depart_time)
    # Calculate and print the total mileage of all trucks.
    total_mileage = print_truck_one.mileage + print_truck_two.mileage + print_truck_three.mileage
    print(f"\nTotal Mileage for All Trucks: {total_mileage:.2f} miles")
    # Print information about all delivered packages.
    print("\nDelivered Packages:")
    delivered_found = False  # Flag to check if any packages are delivered.
    for package_ID in range(1, 41):
        package = print_all_new_table.lookup(package_ID)
        # Check if package is delivered.
        if package and package.status == "Delivered":
            delivered_found = True
            print_information(package)
    # If no packages are delivered, notify the user.
    if not delivered_found:
        print("No packages have been delivered yet.")

# Function to print the status of a specific package at a given time.
def print_specific_package_at_time(print_specific_new_table):
    try:
        # Prompt user to input a specific time to check the package status.
        user_time = input("Enter a time to check the package status (format HH:MM:SS): ").strip()
        h, m, s = user_time.split(":")
        convert_timedelta = timedelta(hours = int(h), minutes = int(m), seconds = int(s))
        # Prompt user to input the package ID.
        package_id = int(input("Enter the numeric package ID: ").strip())
        update_package_9(convert_timedelta)
        package = print_specific_new_table.lookup(package_id)
        if package:
            # Update and print the package's status based on the given time.
            package.update_package_status(convert_timedelta)
            print_information(package)
        else:
            # Notify user if package ID is not found.
            print("Package ID not found.")
    except ValueError:
        # Handle invalid user input
        print("Invalid input. Please try again.")


# Function to print the status of all packages at a given time.
def print_all_packages_at_time(print_all_new_table):
    try:
        # Prompt user to input a specific time to check all package statuses.
        user_time = input("Enter a time to check all package statuses (format HH:MM:SS): ").strip()
        h, m, s = user_time.split(":") # Parse hours, minutes, and seconds from input.
        convert_timedelta = timedelta(hours = int(h), minutes = int(m), seconds = int(s))
        update_package_9(convert_timedelta)
        # Print information about all packages at the given time.
        print(f"\nAll Packages at the Given Time: {convert_timedelta}")
        for packageID in range(1, 41):
            package = print_all_new_table.lookup(packageID)
            if package:
                package.update_package_status(convert_timedelta)
                print_information(package)
    except ValueError:
        # Handle invalid user input.
        print("Invalid input. Please try again.")


# Create truck objects with predefined packages and departure times.
truck_one = Truck(16, 18, None, [13, 14, 15, 16, 19, 20, 1, 29, 30, 31, 34, 37, 40],
                0.0, "4001 South 700 East", timedelta(hours = 8, minutes = 0, seconds = 0))
truck_two = Truck(16, 18, None, [3, 6, 18, 25, 28, 32, 36, 38, 27, 35, 39],
                0.0, "4001 South 700 East", timedelta(hours = 9, minutes = 5, seconds = 0))
truck_three = Truck(16, 18, None, [9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 33],
                0.0, "4001 South 700 East", timedelta(hours = 10, minutes = 20, seconds = 0))

# Load data into the hash table and address/distance lists.
new_table = HashTable()
loaded_new_table = load_package_data("packageCSV.csv", new_table)
loaded_distance_data = load_distance_data("distanceCSV.csv")
loaded_address_data = load_address_data("addressCSV.csv")

# Deliver packages for each truck using a nearest neighbor algorithm.
truck_one.deliver_packages(loaded_new_table, loaded_address_data, loaded_distance_data)
truck_two.deliver_packages(loaded_new_table, loaded_address_data, loaded_distance_data)

# Main class for the program's user interface.
class Main:
    @staticmethod
    def run_ui(ui_new_table, ui_truck_one, ui_truck_two, ui_truck_three):
        while True:
            # Display the menu options for the user.
            print("\nWestern Governors University Parcel Service (WGUPS)")
            print("1. Print All Packages’ Information (Delivered) and Total Mileage")
            print("2. Print Information of a Specific Package at a Given Time")
            print("3. Print Information of All Packages at a Given Time")
            print("4. Exit the Program")
            #  Get the user's menu choice.
            choice = input("Enter your choice (1-4): ").strip()
            if choice == "1":
                # Option 1: Print all delivered packages and total mileage.
                print_all_delivered_packages(ui_new_table, ui_truck_one, ui_truck_two, ui_truck_three)
            elif choice == "2":
                # Option 2: Print information of a specific package at a given time.
                print_specific_package_at_time(ui_new_table)
            elif choice == "3":
                # Option 3: Print information of all packages at a given time.
                print_all_packages_at_time(ui_new_table)
            elif choice == "4":
                # Option 4: Exit the program.
                print("Exiting the program. Goodbye!")
                break
            else:
                # Handle invalid input.
                print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program's user interface.
Main.run_ui(new_table, truck_one, truck_two, truck_three)