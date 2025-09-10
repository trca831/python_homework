#####Task 1 #######
import pandas as pd

# Step 1: Create a DataFrame from a dictionary
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'Los Angeles', 'Chicago']

data = {
    'Name': names,
    'Age': ages,
    'City': cities
}

task1_data_frame = pd.DataFrame(data)
print("Step 1 - Original DataFrame:")
print(task1_data_frame)

# Step 2: Add a new column
task1_with_salary = pd.DataFrame(data)  # beginner might recreate the DataFrame
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\nStep 2 - DataFrame with Salary:")
print(task1_with_salary)

# Step 3: Modify Age column
task1_older = pd.DataFrame(task1_with_salary)  # again re-creating instead of using .copy()
task1_older['Age'] = task1_older['Age'] + 1
print("\nStep 3 - Age increased by 1:")
print(task1_older)

# Step 4: Save as CSV
task1_older.to_csv('employees.csv', index=False)
print("\nStep 4 - Saved as employees.csv")

########Task 2 #########
import pandas as pd
import json

# Step 1: Load data from CSV file
task2_employees = pd.read_csv('employees.csv')
print("Step 1 - Loaded CSV (task2_employees):")
print(task2_employees)

# Step 2: Create a JSON file with additional employees
additional_data = [
    {
        "Name": "Eve",
        "Age": 28,
        "City": "Miami",
        "Salary": 60000
    },
    {
        "Name": "Frank",
        "Age": 40,
        "City": "Seattle",
        "Salary": 95000
    }
]

# Save to JSON file
with open('additional_employees.json', 'w') as f:
    json.dump(additional_data, f, indent=4)

# Load JSON file into a DataFrame
json_employees = pd.read_json('additional_employees.json')
print("\nStep 2 - Loaded JSON (json_employees):")
print(json_employees)

# Step 3: Combine both DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nStep 3 - Combined DataFrame (more_employees):")
print(more_employees)

########Task 3 #########
# Step 1: Use the head() method to get the first three rows
first_three = more_employees.head(3)
print("Step 1 - First Three Rows (first_three):")
print(first_three)

# Step 2: Use the tail() method to get the last two rows
last_two = more_employees.tail(2)
print("\nStep 2 - Last Two Rows (last_two):")
print(last_two)

# Step 3: Get the shape of the DataFrame
employee_shape = more_employees.shape
print("\nStep 3 - Shape of more_employees (employee_shape):")
print(employee_shape)

# Step 4: Use info() method to get summary info
print("\nStep 4 - Info Summary of more_employees:")
more_employees.info()

########Task 4 #########
import pandas as pd
import numpy as np

# Step 1: Load the dirty data CSV into a DataFrame
dirty_data = pd.read_csv('dirty_data.csv')
print("Step 1 - Loaded dirty_data:")
print(dirty_data)

# Optional: Simulate duplicates IN MEMORY ONLY (don’t save to disk)
# print("\nDuplicate row count before cleaning:", dirty_data.duplicated().sum())

# Step 2: Make a copy to clean
clean_data = dirty_data.copy()

# Step 3: Remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("\nStep 3 - After removing duplicates:")
print(clean_data)

# Step 4: Convert 'Age' to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nStep 4 - After converting Age to numeric:")
print(clean_data)

# Step 5: Convert 'Salary' to numeric and replace placeholders with NaN
clean_data['Salary'] = pd.to_numeric(
    clean_data['Salary'].replace(['unknown', 'n/a'], np.nan),
    errors='coerce'
)
print("\nStep 5 - After converting Salary to numeric and replacing placeholders:")
print(clean_data)

# Step 6: Fill missing numeric values
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("\nStep 6 - After filling missing Age and Salary values:")
print(clean_data)

# Step 7: Convert 'Hire Date' to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
clean_data = clean_data[clean_data['Hire Date'].notna()]
print("\nStep 7 - After converting Hire Date to datetime:")
print(clean_data)

# Step 8: Strip whitespace and standardize text
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print("\nStep 8 - After cleaning Name and Department columns:")
print(clean_data)