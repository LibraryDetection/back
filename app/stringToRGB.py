import base64
import io
from PIL import Image
import numpy as np

def stringToRGB(base64_string):
    imgdata = base64.b64decode(base64_string)
    dataBytesIO = io.BytesIO(imgdata)
    image = Image.open(dataBytesIO)
    resized_image = image.resize((1104, 1080))
    return resized_image