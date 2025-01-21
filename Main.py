import HashTable
import Package
import Truck
import csv
from datetime import datetime, timedelta



TRUCK_SPEED = 18/60 # miles per minute from 18 mph
print("The Truck Speed = %.2f miles per minute" % TRUCK_SPEED)

TODAY = datetime.now()

print(TODAY)
START = datetime(TODAY.year, TODAY.month, TODAY.day, 8,0,0,0,)

def load_package_data(package_file, hash_table):
    with open(package_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            package = Package()
            package.unique_id = int(str.strip(row[0]))
            package.truck = None
            package.info = [str.strip(x) for x in row[1::]]
            package.status = 'Hub'
            package.time_delivered = None
            hash_table.insert(package.id, package)
    return hash_table

L_hash_table = HashTable(Package)













