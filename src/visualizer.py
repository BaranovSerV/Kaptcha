import matplotlib.pyplot as plt


class Visualizer:
    @staticmethod
    def show_image(image):
        """Выводит изображение в виде точек."""
        plt.figure(figsize=(6, 6))
        plt.xlim(len(image), 0)
        plt.ylim(len(image), 0)
        plt.grid()
        
        for i in range(len(image)):
            for j in range(len(image)):
                if image[i, j] >= 0.9:
                    plt.plot(j, i, color="green", marker="o", markersize=7)
        
        plt.show()

