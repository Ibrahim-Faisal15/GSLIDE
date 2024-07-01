from dotenv import load_dotenv
from pexels_api import API
import os
import requests







load_dotenv()
IMG_API =  os.getenv('PEXEL_API_KEY')
IMG_API = API(IMG_API)

def get_image(topic):
    if not os.path.exists('images'):
        os.makedirs('images')
    photos = IMG_API.search(topic)
    for index, photo in enumerate(photos['photos'], start=1):
        image_url = photo['src']['large']
        image_filename = f'images/{index}.jpg' 

        response = requests.get(image_url)
        response.raise_for_status()

        with open(image_filename, 'wb') as file:
            file.write(response.content)

        print(f"Image saved: {image_filename}")










