import numpy as np
from tabulate import tabulate

from image_processor import ImageProcessor
from orthogonal_recognizer import OrthogonalRecognizer
from corrector import Corrector
from visualizer import Visualizer


if __name__ == "__main__":
    symbols = ImageProcessor("Symbols")
    
    recognizer = OrthogonalRecognizer(symbols.images)

    
    distorted = ImageProcessor("Distorted")
    
    corrector = Corrector(distorted.images, recognizer)

    
    max_iter = int(input("Введите количество итераций: "))
    img_idx = int(input("Введите номер искаженного изображения: "))
    
    corrected_img, iter_count = corrector.correct_image(img_idx, max_iter)
    
    print(f"Исправлено за {iter_count} итераций")

    print(tabulate(np.matrix.round(corrected_img), numalign="right"))
    
    Visualizer.show_image(corrected_img)


