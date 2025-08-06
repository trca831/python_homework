#Task3

import csv

with open("../csv/employees.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

names = [row[0] + " " + row[1] for row in rows[1:]]

names_with_e = [name for name in names if "e" in name or "E" in name]

print(names)
print(names_with_e)