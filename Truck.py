class Truck(object):

    def __init__(self, packages = None, location = None, current_time = None, time_left_hub = None):
        self.packages = packages
        self.location = location
        self.current_time = current_time
        self.time_left_hub = time_left_hub
        return

    def load_truck_packages(self, package_numbers_list, hash_table):
        package_list = []
        for i in package_numbers_list:
            i = int(i)
            hash_table.find(i).status = 'Transit'
            package_list.append(hash_table.find(i))
        return package_list
