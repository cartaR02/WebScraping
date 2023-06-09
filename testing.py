import requests
from bs4 import BeautifulSoup

url = "https://www.fmc.com/en/news-media/company-news"  # Replace with the URL of the website
documents = {}  # Dictionary to store titles and dates

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant elements on the page and extract information
# Adjust the selectors and extraction logic based on the structure of the website

# Example: Extract all titles and dates within the div element
div_elements = soup.find_all("div")  #wdawdawdawd Adjust the selector based on the div elements containing titles and dates

for div_element in div_elements:
    title_element = div_element.find("div", class_="card-content--title")  # Adjust the selector for the title element
    date_element = div_element.find("div", class_="byline-date")  # Adjust the selector for the date element

    if title_element and date_element:
        title = title_element.text.strip()
        date = date_element.text.strip()
        documents[title] = date  # Add the title and date to the dictionary

# Check if any documents were found
if len(documents) == 0:
    print("No documents were found on the website.")
else:
    # Print and save the extracted titles and dates
    with open("documents.txt", "w") as file:
        for title, date in documents.items():
            file.write(f"Title: {title} | Date: {date}\n")
            print(f"Title: {title} | Date: {date}")

    print("Data has been saved to documents.txt file.")
