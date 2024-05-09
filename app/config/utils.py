import os
import dotenv
import requests

dotenv.load_dotenv()



def save_image(image,content_type):
    url = f"{os.getenv('IMAGE_SERVICE_URL')}/images/"

    image_file = ('image',image,content_type)

    files = {'image': image_file}

    try:
        response = requests.post(url, files=files)
        print(response.request.headers)
        response.raise_for_status()
    except requests.HTTPError as err:
        return {
            'data': {
                "error": "File is not a image",
                "message": response.json()
            }
        }
    else:
        return response.json()

