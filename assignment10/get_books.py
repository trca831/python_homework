# get_books.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import json
import os

# Step 1: Set up Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the search page
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

# Optional: wait a few seconds for page to load
time.sleep(3)

# Step 2: Find all <li> entries for search results
# --------------------------
# Use the class from Task 2 notes: "row cp-search-result-item"
li_elements = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
print(f"Found {len(li_elements)} search results")


# Step 3: Extract data
results = []

for li in li_elements:
    # Title
    try:
        title_elem = li.find_element(By.CSS_SELECTOR, "a.cp-title-link")
        title = title_elem.text
    except:
        title = ""
    
    # Authors 
    try:
        author_elems = li.find_elements(By.CSS_SELECTOR, "a.author-link")
        authors = "; ".join([a.text for a in author_elems])
    except:
        authors = ""
    
    # Format & Year
    try:
        format_year_elem = li.find_element(By.CSS_SELECTOR, "div.cp-format-year")
        format_year = format_year_elem.text
    except:
        format_year = ""
    
    # Store in dict
    book_dict = {
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    }
    
    results.append(book_dict)

# Step 4: Create DataFrame and print
df = pd.DataFrame(results)
print(df)

# Optional: save to CSV or JSON
df.to_csv("durham_library_books.csv", index=False)
df.to_json("durham_library_books.json", orient="records", indent=2)

# Close the browser
driver.quit()


# Make sure the assignment10 folder exists
output_folder = "assignment10"
os.makedirs(output_folder, exist_ok=True)

# File paths
csv_path = os.path.join(output_folder, "get_books.csv")
json_path = os.path.join(output_folder, "get_books.json")

# Save DataFrame to CSV
df.to_csv(csv_path, index=False)
print(f"DataFrame saved to {csv_path}")

# Save results list to JSON
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
print(f"Results saved to {json_path}")