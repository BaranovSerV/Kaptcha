import numpy as np

class Corrector:
    def __init__(self, distorted_images, recognizer):
        self.distorted_images = distorted_images
        self.recognizer = recognizer

    def correct_image(self, image_idx, max_iter=10):
        """Исправляет изображение методом ортогональной проекции."""
        Q = self.distorted_images[image_idx]
        iter_count = 0

        while iter_count < max_iter:
            for i, v_sopr in enumerate(self.recognizer.sopr_vectors):
                if np.sum(Q * v_sopr) == np.sum(self.recognizer.images[i] * v_sopr):
                    return Q, iter_count + 1

            Q = self._di(Q)

            iter_count += 1


        return Q, iter_count

    def _di(self, Q):
        """Выполняет одну итерацию коррекции."""
        B = np.zeros_like(Q)
        C = np.zeros_like(Q)

        for i, v_sopr in enumerate(self.recognizer.sopr_vectors):
            B += np.sum(v_sopr * Q) * (self.recognizer.V[i] + Q * (-1.0))
            
            for j, _ in enumerate(self.recognizer.sopr_vectors):
                if j != i:
                    C += (np.sum(v_sopr * Q) ** 2) * np.sum(self.recognizer.sopr_vectors[j] * Q) * self.recognizer.V[j]
        
        return Q + B - C

