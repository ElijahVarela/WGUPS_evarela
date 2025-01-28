from datetime import timedelta

# Class representing a delivery truck with routing and package management capabilities
class Truck:
    def __init__(self, capacity, truck_speed, load, packages, mileage, address, depart_time):
        self.capacity = capacity
        self.truck_speed = truck_speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.current_time = depart_time
        self.current_location = address

    # Returns formatted string with key truck operational details.
    def __str__(self):
        return (
            f"Capacity: {self.capacity}, "
            f"Truck Speed: {self.truck_speed}, "
            f"Load: {self.load}, "
            f"Packages: {self.packages}, "
            f"Mileage: {self.mileage}, "
            f"Address: {self.address}, "
            f"Depart Time: {self.depart_time}, "
            f"Current Location: {self.current_location}, "
            f"Current Time: {self.current_time}"
        )

    # Calculates distance between two addresses using distance matrix data.
    def distance_between(self, address1, address2, address_data, distance_data):
        # Check if both addresses exist in the address database.
        if address1 not in address_data or address2 not in address_data:
            print('One or both locations is invalid')
            return
        else:
            # Get indices for distance matrix lookup.
            i = address_data.index(address1)
            j = address_data.index(address2)
            if i > j:
                return distance_data[i][j]
            else:
                return distance_data[j][i]

    # Manages package delivery process using nearest neighbor algorithm
    def deliver_packages(self, new_table, address_data, distance_data):
        # Set initial departure time for all loaded packages
        for package_id in self.packages:
            package = new_table.lookup(package_id)
            if package:
                package.departure_time = self.depart_time
        # Continue deliveries until all packages are delivered.
        while len(self.packages) > 0:
            min_distance = float('inf')
            closest_package = None
            # Find nearest undelivered package.
            for package_id in self.packages:
                package = new_table.lookup(package_id)
                route_distance = self.distance_between(
                    self.current_location, package.address, address_data, distance_data
                )
                # Update closest package candidate
                if route_distance < min_distance:
                    min_distance = route_distance
                    closest_package = package
            if not closest_package:
                break  # Exit if no valid package
            # Update mileage, time, and package status.
            self.mileage += min_distance
            travel_time = timedelta(hours=min_distance / self.truck_speed)
            self.current_time += travel_time

            # Update package delivery information.
            closest_package.delivery_time = self.current_time
            closest_package.status = "Delivered"

            # Move truck to new location and remove delivered package.
            self.current_location = closest_package.address
            self.packages.remove(closest_package.package_id)