import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def code_extract(url):
# url = "https://www.screener.in/company/BRITANNIA/consolidated/"
    # Use a regular expression to extract the company name
    match = re.search(r'/company/([^/]+)/', url)

    if match:
        company_name = match.group(1)
        return company_name
    else:
        return ""

# URL pattern for all pages
base_url = "https://www.screener.in/screens/357649/all-listed-companies/?page="

# Lists to store the scraped data
data = []

# Loop through all 96 pages
for page in range(97, 193):
    url = base_url + str(page)
    print(f"Fetching page {page}...")
    # Send HTTP request to the page
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page {page}")
        continue

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table that contains the data
    table = soup.find('table', class_='data-table text-nowrap striped mark-visited')

    if not table:
        print(f"No table found on page {page}")
        continue

    # Iterate over the rows in the table
    rows = table.find('tbody').find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]  # Get the text content of each cell

        # Check if the name column and the URL exist
        name_column = row.find('td', class_='text')
        if name_column and name_column.find_next_sibling('td'):
            company_name = name_column.find_next_sibling('td').text.strip()
            company_url = name_column.find_next_sibling('td').find('a')['href']
            company_url = "https://www.screener.in" + company_url  # Complete the URL

            # Insert company name and URL into the data
            cols[1] = company_name
            cols.insert(2, company_url)  # Insert URL after company name
            cols.insert(3, code_extract(company_url))  # Insert code after URL

            data.append(cols)
        else:
            print(f"Skipping a row due to missing name or URL on page {page}")
            continue

    # Wait for a while to avoid overwhelming the server with requests
    time.sleep(1)

# Define the column names for the CSV
columns = ["S.No", "Name", "URL", "Exchange Code", "CMP Rs.", "P/E", "Mar Cap Rs.Cr.", "Div Yld %", "NP Qtr Rs.Cr.", "Qtr Profit Var %", "Sales Qtr Rs.Cr.", "Qtr Sales Var %", "ROCE %"]

# Create a DataFrame from the scraped data
df = pd.DataFrame(data, columns=columns)

# Save the data to a CSV file
df.to_csv('listed_companies_with_urls_2.csv', index=False)

print("Data scraping complete. CSV saved as 'listed_companies_with_urls.csv'.")
