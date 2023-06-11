import requests
from bs4 import BeautifulSoup

websites = {
    "https://www.aerotek.com/en/about-us/news-and-events/news/2023/05/aeroteks-david-jordan-named-to-2023-sia-dei"
    "-influencers": {
        "title_selector": "h1.acs-page-title",
        "date_selector": "p.acs-page-date",
    }, "https://www.fmc.com/en/news-media/company-news": {
        "title_selector": "div.card-content--title",
        "date_selector": "div.byline-date",
    }
    # Add more websites and their selectors as needed
}

documents = {}  # Dictionary to store titles and dates

# Iterate over the websites
for website, selectors in websites.items():
    # Send a GET request to the URL
    response = requests.get(website)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the titles and dates using the respective selectors
    title_elements = soup.select(selectors["title_selector"])
    date_elements = soup.select(selectors["date_selector"])

    # Check if the number of titles and dates match
    if len(title_elements) != len(date_elements):
        print(f"Error: Mismatch between the number of titles and dates on {website}")
        continue

    # Extract the titles and dates and store them in the dictionary
    for title_element, date_element in zip(title_elements, date_elements):
        title = title_element.text.strip()
        date = date_element.text.strip()
        documents[title] = date

    # Check if any documents were found
    if len(documents) == 0:
        print(f"No documents were found on the website: {website}")
    else:
        # Print and save the extracted titles and dates
        with open("documents.txt", "a") as file:  # Append to the file
            for title, date in documents.items():
                file.write(f"Title: {title} | Date: {date}\n")
                print(f"Title: {title} | Date: {date}")

print("Data has been saved to documents.txt file.")
