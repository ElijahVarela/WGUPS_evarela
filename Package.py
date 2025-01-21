from optparse import IndentedHelpFormatter


class Package:

    def __inti__(self, ID = None, INFO = None, TRUCK = NONE, STATUS = 'HUB', timeLoaded = None, timeDelivered = None):
        self.ID = ID
        self.INFO = INFO
        self.TRUCK = TRUCK
        self.STATUS = STATUS
        self.timeLoaded = timeLoaded
        self.timeDelivered = timeDelivered
        return

    # Print pacakge details
    def printPackage(self):
        print("\n\nPackage ID = ", self.ID)
        print("Package Details = ", self.INFO)
        print("Truck of Package = ", self.TRUCK)
        print("Status of Package = ", self.STATUS)
        print("Time Pacakge Loaded = ", self. timeLoaded)
        print("Time Package Delivered = ", self.timeDelivered)
        return