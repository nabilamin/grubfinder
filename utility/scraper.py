from bs4 import BeautifulSoup
import requests

# Function to get the first 9 images from a restaurant's Yelp page
def get_images(restaurant_name):
    # URL takes in the restaurant name + city as a parameter
    URL = f"https://www.yelp.com/biz_photos/{restaurant_name}?tab=food"
    # request the page and parse it
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Find the div containing the images and grab the divs with the images
    img_container = soup.find("div", class_="media-landing_gallery")
    images = img_container.find_all("img")

    # Return the src attribute of the first 9 images
    return [photo.get("src") for photo in images[:9]]

# print(get_images("gyuzo-japanese-bbq-rockville"))