#Task2

import csv
import traceback

def read_employees():
    data = {}          
    rows = []          

    try:
        with open("../csv/employees.csv", "r", newline="") as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
        data["rows"] = rows
        return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace.filename} , Line : {trace.lineno}, Func.Name : {trace.name}, Message : {trace.line}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

employees = read_employees()

print(employees)

#Task3

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

#Task4

def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

#Task5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task6

def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

#Task7

def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]

#Task8

def employee_dict(row):
    return {key: value for key, value in zip(employees["fields"], row) if key != "employee_id"}

#Task9

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[0]
        emp_data = employee_dict(row)
        result[emp_id] = emp_data
    return result

#Task10

import os  

def get_this_value():
    return os.getenv("THISVALUE")

#Task11

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

#Task12

import csv
import traceback

def read_csv_to_dict(filename):
    data = {}
    rows = []
    try:
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(tuple(row))  
        data["rows"] = rows
        return data
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace.filename} , Line : {trace.lineno}, Func.Name : {trace.name}, Message : {trace.line}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print("Minutes1:", minutes1)
print("Minutes2:", minutes2)


#Task13

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined_set = set1.union(set2)  
    return combined_set

minutes_set = create_minutes_set()


#Task14

from datetime import datetime

def create_minutes_list():
    minutes = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes))
    return converted

minutes_list = create_minutes_list()

#Task15

import csv
from datetime import datetime

def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list

write_sorted_list()
