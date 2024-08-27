"""utils for this proyect"""
import os
import dotenv
import requests

dotenv.load_dotenv()



def save_image(image,content_type):
    """
        save image to image service
        if status message is not 200, raise an exception

        :param image: image file
        :param content_type: image content type
    """
    url = f"{os.getenv('IMAGE_SERVICE_URL')}/images/"

    image_file = ('image',image,content_type)

    files = {'image': image_file}

    try:
        response = requests.post(url, files=files, timeout=5)

        response.raise_for_status()
        return response.json()
    except requests.HTTPError as error:
        print(error)
        raise ValueError(
            "Don't save image in image service"
        ) from error
