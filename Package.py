class Package:

    def __inti__(self, unique_id = None, info = None, truck = None, status = 'HUB', time_loaded = None, time_delivered = None):
        self.unique_id = unique_id
        self.info = info
        self.truck = truck
        self.status = status
        self.time_loaded = time_loaded
        self.time_delivered = time_delivered
        return

    # Print pacakge details
    def print_package(self):
        print("\n\nPackage ID = ", self.unique_id)
        print("Package Details = ", self.info)
        print("Truck of Package = ", self.truck)
        print("Status of Package = ", self.status)
        print("Time Pacakge Loaded = ", self. time_loaded)
        print("Time Package Delivered = ", self.time_delivered)
        return


myPackage = Package()