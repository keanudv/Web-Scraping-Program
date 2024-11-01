# Import the libraries
import requests
from bs4 import BeautifulSoup

# Defines a function to scrape data
def scrape_costco_data():

    # The target webpage
    url = "https://www.costco.com/diet-nutrition.html"

    # Headers to mimic a browser request
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

    # Creates a variable (response) to store the results of the HTTP GET request
    response = requests.get(url, headers=headers)

    # Checks if the request was successful (200 status code)
    if response.status_code == 200:

        # If successful, parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate each product
        product_containers = soup.find_all("div", class_="product")

        # Creates an empty list to store product information
        products = []

        # Loops through each product to extract the name and price
        for product in product_containers:
            # Extract the product name
            html_name_element = product.find("span", class="description")
            name = html_name_element.text.strip() if html_name_element else "Name Not Found"

            # Extract the product price
            html_price_element = product.find("div", class_="price")
            price = html_price_element.text.strip() if html_price_element else "Price Not Found"

            # Add the product name and price to the empty list
            products.append(
                {
                    "name": name,
                    "price": price
                }
            )

        # Print out the product names and prices
        for i, product in enumerate(products, 1):
            print(f"{i}. {product['name']} - {product['price']}")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Run the function to scrape the data
if __name__ == "__main__":
    scrape_costco_data()
