"""
Sessions service contains functions required to create and manage sessions.
"""

import os
import random
import requests
from bs4 import BeautifulSoup

def yelp_search(data):
    '''
    Executes a search against yelp's API.
    '''
    url = _yelp_search_url_builder(data['location'], data['price'], data['open_at'])

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + _get_yelp_key()
    }

    response = requests.get(url, headers=headers, timeout=10)

    return response

def create_random_id() -> int:
    '''
    Returns a random 6 digit ID
    '''
    return random.randint(100000, 999999)

def validate_session_create_data(data) -> bool:
    '''
    Validates user data input for session creation
    '''
    print(type(data))

def parse_transactions(transactions: list) -> tuple[bool, bool]:
    '''
    Parses restaurant transaction types to determine if the restaurant does delivery or pick up.

    Returns: Tuple[pickup: bool, delivery: bool]
    '''
    pickup = False
    delivery = False

    for transaction in transactions:
        if transaction == 'pickup':
            pickup = True
        if transaction == 'delivery':
            delivery = True
    
    return pickup, delivery

def _yelp_search_url_builder(location: str, price: int, open_at: str):
    '''
    Builds the url string to get a list of restaurants from.
    '''
    base_url = f'https://api.yelp.com/v3/businesses/search?location={location}&price={price}&term=restaurants&sort_by=rating&limit=10'

    if open_at != '':
        # todo: convert time stamp to unix time per yelp api docs
        pass

    return  base_url

def _get_yelp_key():
    '''
    Gets the api key from aws secret manager to use when requesting data from yelp's API.
    '''
    return os.environ.get('YELP_KEY')

def get_images(restaurant_alias) -> list[str]:
    """
    Scrape images from yelp.
    Gets the first 9 images from a restaurant's Yelp page.

    Function developed by Tristan Zimmerman.
    """
    # URL takes in the restaurant name + city as a parameter
    url = f"https://www.yelp.com/biz_photos/{restaurant_alias}?tab=food"
    
    # request the page and parse it
    response = requests.get(url, timeout = 10)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    # Find the div containing the images and grab the divs with the images
    img_container = soup.find("div", class_="media-landing_gallery")
    images = img_container.find_all("img")

    # Return the src attribute of the first 9 images
    return [photo.get("src") for photo in images[:9]]