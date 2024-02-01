
from matplotlib import pyplot as plt
import numpy as np


def plot_eq(img, eq=False, opencv=False):
    _, ax = plt.subplots(1, 2, figsize=(12, 6))
    title = 'Imagen ecualizada' if eq or opencv else 'Imagen con escala de grises'
    title2 = 'Histograma con distribución ecualizada' if eq or opencv else 'Histograma'
    title3 = 'Distribución Acumulada Ecualizada' if eq or opencv else 'Distribución Acumulada'

    hist, _ = np.histogram(img.flatten(), 256, [0,256])
    fda = hist.cumsum() # Funcion de distribucion acumulada (FDA)

    if not opencv:
        if eq:
            fda_norm = (fda - fda.min()) * 255 / (fda.max() - fda.min())

            img = fda_norm[img.flatten()].reshape(img.shape) # Mapeando los valores de la imagen
            hist, _ = np.histogram(img.flatten(), 256, [0,256])
            fda = hist.cumsum()
            
    fda_norm = fda * hist.max() / fda.max()


    ax[0].imshow(img, cmap='gray')
    ax[0].axis('off')
    ax[0].set_title(title)

    ax[1].hist(img.ravel(), bins=256, range=[0,256], label=title2)
    ax[1].plot(fda_norm, label=title3)
    ax[1].set_xlabel('Valor del pixel')
    ax[1].set_ylabel('Frecuencia')

    ax[1].legend()
    plt.tight_layout()
    plt.show()

