"""
LaplicianEdgeDetection
"""
import cv2
import numpy as np


class LapliacianEdgeDetection:

    def __init__(self, image):
        self.image = image
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def edge(self):
        # Applying Gaussian Blur to reduce the noise of the image
        img_pad = cv2.GaussianBlur(self.gray_image, (3, 3), 0)

        # Performing laplacian edge detection
        laplacian_image = cv2.Laplacian(img_pad, cv2.CV_8U, ksize=3)

        # Flipping the image so that kivy displays it correctly
        image = cv2.flip(laplacian_image, 0)

        return np.array(image)
