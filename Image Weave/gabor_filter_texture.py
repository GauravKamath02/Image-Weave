from skimage import data, io, filters
import numpy as np
from scipy import ndimage as ndi
from skimage.filters import gabor_kernel
from skimage.color import gray2rgba
import cv2


class GaborFilterTexture:
    def __init__(self, image):
        self.image = image
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def detect(self):
        kernels = []
        for theta in range(4):
            theta = theta / 4. * np.pi
            for sigma in (1, 3):
                kernel = np.real(gabor_kernel(0.5, theta=theta, sigma_x=sigma, sigma_y=sigma))
                kernels.append(kernel)

        # Apply the Gabor filters
        filtered = []
        for kernel in kernels:
            filtered.append(ndi.convolve(self.gray, kernel, mode='wrap'))

        # Compute the mean response for each filter
        mean_responses = np.array([np.mean(img) for img in filtered])
        lbp_image_rgba = gray2rgba(mean_responses)

        return lbp_image_rgba
