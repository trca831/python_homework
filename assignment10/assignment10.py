# Task 1: Reviewed https://durhamcountylibrary.org/robots.txt
# General scraping of public pages is allowed. Only /staff/ is disallowed.
# Ensuring compliance by not accessing restricted areas and scraping responsibly.

import pandas as pd
import json

# Suppose your data is in a list of dictionaries like this:
results = [
    {"title": "Book 1", "author": "Author A", "year": 2020},
    {"title": "Book 2", "author": "Author B", "year": 2021},
    # ... more books
]

# Convert list of dicts to a DataFrame
df = pd.DataFrame(results)

# Write to CSV
csv_path = "python_homework/assignment10/get_books.csv"
df.to_csv(csv_path, index=False)
print(f"CSV written to {csv_path}")

# Write to JSON
json_path = "python_homework/assignment10/get_books.json"
with open(json_path, "w") as f:
    json.dump(results, f, indent=4)
print(f"JSON written to {json_path}")