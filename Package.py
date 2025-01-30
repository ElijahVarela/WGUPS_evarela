# Class for representing a package with tracking information and delivery details.
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.departure_time = None
        self.delivery_time = None
        self.status = "At Hub"

    # Returns formatted string with key package details for display purposes.
    def __str__(self):
        return (
            f"Address: {self.address}, "
            f"City: {self.city}, "
            f"State: {self.state}, "
            f"Zipcode: {self.zip_code}, "
            f"Deadline: {self.deadline}, "
            f"Weight: {self.weight}, "
            f"Notes: {self.notes}, "
        )

    # Updates package status based on current simulation time comparison.
    def update_package_status(self, convert_timedelta):
        # Check if package has been delivered.
        if self.delivery_time is not None and self.delivery_time <= convert_timedelta:
            self.status = "Delivered"
        # Check if package is en route.
        elif self.departure_time is not None and self.departure_time <= convert_timedelta:
            self.status = "En Route"
        # Default to at-hub status.
        else:
            self.status = "At Hub"

