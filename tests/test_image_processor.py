import numpy as np

from ..src.image_processor import ImageProcessor


def test_load_images(temp_images_dir):
    processor = ImageProcessor(temp_images_dir)
    
    assert len(processor.images) == 2
    
    white_img_processed = processor.images[0]  
    expected_white = np.zeros((2, 2), dtype=np.uint8)
    assert np.array_equal(white_img_processed, expected_white)
    
    black_img_processed = processor.images[1]
    expected_black = np.ones((2, 2), dtype=np.uint8)
    assert np.array_equal(black_img_processed, expected_black)


def test_pixel_values(temp_images_dir):
    processor = ImageProcessor(temp_images_dir)
    
    for img in processor.images:
        unique_values = np.unique(img)
        assert np.all(np.isin(unique_values, [0, 1]))


def test_empty_directory(tmpdir):
    empty_dir = tmpdir.mkdir("empty")
    processor = ImageProcessor(empty_dir.strpath)
    
    assert len(processor.images) == 0
