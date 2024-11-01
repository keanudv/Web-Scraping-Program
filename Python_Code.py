# Import the libraries
import requests
from bs4 import BeautifulSoup

# Defines a function to scrape data
def scrape_data():

    # The target webpage
    url = "https://www.costco.com/diet-nutrition.html"

    # Headers to mimic a browser request
    headers = {"'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

    # Creates a variable (response) to store the results of the HTTP GET request
    response = requests.get(url, headers=headers)

    # Checks if the request was successful (200 status code)
    if response.status_code == 200:

        # If successful, parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Looks for product descriptions by class name
        product_elements = soup.find_all('span', class_='description')

        # Prints the first 1000 characters of the HTML content for inspection
        print(soup.prettify()[:1000])

        # Extract the data (use the correct selector)
        titles = soup.find_all('span', class_='titleline')

        # Print the extracted titles
        if titles:
            for i, title in enumerate(titles, 1):
                print(f"{i}. {title.text}")
        else:
            print("No titles found. Check the class name in the HTML structure.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Run the function to scrape the data
if __name__ == "__main__":
    scrape_data()
