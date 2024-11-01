# Import the libraries
import requests
from bs4 import BeautifulSoup

# Creates a function top scrape data
def scrape_data():
  
    # The target webpage url
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    # Checks if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Print a sample of the HTML content to identify the correct class name
        print(soup.prettify()[:1000])  # Print the first 1000 characters for inspection

        # Extract the data (use the correct selector)
        titles = soup.find_all('span', class_='titleline')  # Ensure this matches the actual class name

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
