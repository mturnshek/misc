import simplejson
import urllib
import googlemaps
from openpyxl import Workbook, load_workbook
import time

# excel files with rows of entries
# cols: Full Name, Company Name, City, Zip Code, Email, Phone, Membership Start Date, Membership Expiration Date
# filenames = ["ex1.xlsx", "ex2.xlsx", "ex3.xlsx"]
filenames = []

# Read files into list
targets = []
for filename in filenames:
	wb = load_workbook(filename)
	ws = wb.active
	for row in ws.rows:
		entry = []
		for cell in row:
			entry.append(cell.value)
		targets.append(entry)

# Clean targets
cleaned = []
for entry in targets:
	# only keep those who have provided Name, City, ZIP, and email
	if not entry[0].isspace() and not entry[2].isspace() and not entry[3].isspace() and not entry[4].isspace():
		cleaned.append([str(entry[0]), str(entry[2]), str(entry[3]), str(entry[4])]) # name, city, zip, email
targets = cleaned

# test set
# targets = [["Matt", "Pittsburgh", "15217", "example@gmail.com"],
# 		   ["Bob", "Philadelphia", "19102", "example@gmail.com"]]

# Compute which targets are in range using googlemaps API
max_distance = 80000 # meters away which you can be and still appear on the list
destination = "Allegheny Observatory, Pittsburgh, PA"

i = 0
for entry in targets:
	print i, " of ", len(targets)
	origin = entry[1] + ", " + entry[2]
	url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(origin, destination)
	result = simplejson.load(urllib.urlopen(url))

	try:
		target_distance = result['rows'][0]['elements'][0]['distance']['value']
	except:
		print "error for:\n", entry, result
		target_distance = 9999999999 # intentionally large
	if target_distance < max_distance:
		entry.append(True)
	else:
		entry.append(False)
	i += 1
	time.sleep(1)

# Entry: [Name, City, ZIP, email, Bool for within distance]
print len(targets)
targets = filter(lambda x: x[4], targets) # Removes entries which were too far away
print len(targets)

# Write entries which are close enough to a list
filename = "within_distance.txt"
target = open(filename, 'w')
for entry in targets:
	target.write(entry[3])
	target.write("\t\t\t")
	target.write(entry[0])
	target.write("\n")
target.close()