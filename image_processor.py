import os
from PIL import Image, ImageOps

import numpy as np


class ImageProccessor:
    def __init__(self, directory: str):
        self.directory = directory


    def load_images(self):
        images = []

        files = os.listdir(self.directory)
        
        for file in files:
            path = os.path.join(self.directory, file)

            img = Image.open(path).convert('L')
            img_inverted = ImageOps.invert(img)
            binary_img = np.array(img_inverted)
            binary_img[binary_img > 0] = 1
            
            images.append(binary_img)
        
        return images

