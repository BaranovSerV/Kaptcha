import numpy as np

class OrthogonalRecognizer:    
    def __init__(self, images):
        self.images = [img.astype(np.float64) for img in images]
        self.n = len(self.images)

        self.V = self._compute_V()
        self.A = np.linalg.inv(self.V)  
        self.sopr_vectors = self._compute_sopr_vectors()

    def _compute_V(self):
        n = self.n
        V = np.zeros((n, n), dtype=np.float64)  
        
        for i in range(n):
            for j in range(n):
                V[i, j] = np.sum(self.images[i] * self.images[j])
        return V

    def _compute_sopr_vectors(self):
        n = self.n
        sopr_vectors = []

        for i in range(n):
            v_sopr = np.zeros_like(self.images[0])
            for j in range(n):
                v_sopr += self.A[i, j] * self.images[j]

            sopr_vectors.append(v_sopr)
        return sopr_vectors
