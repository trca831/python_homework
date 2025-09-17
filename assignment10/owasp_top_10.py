from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Setup Selenium (make sure you have ChromeDriver installed and in PATH)
driver = webdriver.Chrome()

# Open the OWASP Top 10 page
driver.get("https://owasp.org/www-project-top-ten/")

# Give the page a few seconds to load
time.sleep(3)

# Find the top 10 vulnerabilities
# Inspect the page: titles are in <h3> within <div class="views-row">
vuln_elements = driver.find_elements(By.XPATH, '//div[contains(@class,"views-row")]//h3/a')

top_10_list = []

for vuln in vuln_elements:
    title = vuln.text
    link = vuln.get_attribute('href')
    top_10_list.append({"title": title, "link": link})

# Print the list
for item in top_10_list:
    print(item)

# Write to CSV
with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "link"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for item in top_10_list:
        writer.writerow(item)

# Close the browser
driver.quit()