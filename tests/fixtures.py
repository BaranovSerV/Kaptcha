import pytest
import numpy as np
from PIL import Image
from pathlib import Path

from ..src.image_processor import ImageProcessor

@pytest.fixture
def temp_images_dir(tmpdir):

    white_img = Image.new('L', (2, 2), 255)  

    black_img = Image.new('L', (2, 2), 0)   
    
    # Сохраняем во временную директорию
    white_path = tmpdir.join("white.png")
    black_path = tmpdir.join("black.png")

    white_img.save(white_path)
    black_img.save(black_path)
    
    return Path(tmpdir.strpath)
