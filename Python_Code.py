# Import the libraries
import requests
from bs4 import BeautifulSoup

# Defines a function to scrape product name and price data
def scrape_data(url, name_tag, name_class, price_tag, price_class):
    '''
    This function scrapes product name and price data from a given website.

    Parameters:
    1. url - The target webpage URL.
    2. name_tag - The HTML tag for the product name.
    3. name_class - The HTML class for the product name.
    4. price_tag - The HTML tag for the price name.
    5. price_class - The HTML class for the price name.

    Returns:
    Show the name and price of each product that appears on a webpage.
    '''

    # Headers to mimic a real browser request
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
    '''
    This is needed because some sites block requests that do not come from a real user's browser.
    By changing the headers to include a User-Agent string, we can bypass the restrictions.
    '''

    # Creates a variable (response) to store the results of the HTTP GET request
    response = requests.get(url, headers=headers)

    # Checks if the request was successful (200 status code)
    if response.status_code == 200:

        # If successful, parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Creates an empty list to store product information
        products = []

        # Loops through each product to extract the name and price
        for product in soup.find_all(name_tag, class_=name_class):
            # Extract the product name
            name = product.text.strip() if product else "Name Not Found"

            # Extract the product price
            price_element = product.find_next(price_tag, class_=price_class)
            price = price_element.text.strip() if price_element else "Price Not Found"

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

    # If not successful, show the error
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Run the function to scrape the data
if __name__ == "__main__":
    scrape_data(
        url="target URL", 
        name_tag="html name tag", 
        name_class="html name class", 
        price_tag="html price tag", 
        price_class="html price class"
    )

# Costco example
if __name__ == "__main__":
    scrape_data(
        url="https://www.costco.com/diet-nutrition.html", 
        name_tag="span", 
        name_class="description", 
        price_tag="div", 
        price_class="price"
    )

# Foodland example
if __name__ == "__main__":
    scrape_data(
        url="https://shop.foodland.com/sm/planning/rsid/11/categories/fruits-vegetables/fresh-fruits-id-47", 
        name_tag="div", 
        name_class="ProductCardstyles__DivKeyboardHandled-sc-fhu8gl-0 cjvWLW", 
        price_tag="span",
        price_class="ProductCardPrice--1sznkcp jwMPxX"
    )
