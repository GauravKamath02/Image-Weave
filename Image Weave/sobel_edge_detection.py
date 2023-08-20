"""
Sobel Edge Detection
"""
import cv2
import numpy as np


class SobelEdgeDetection:

    def __init__(self, image):
        self.image = image
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def edge(self):
        sobelx = cv2.Sobel(self.gray_image, cv2.CV_8U, 1, 0, ksize=3)
        sobely = cv2.Sobel(self.gray_image, cv2.CV_8U, 0, 1, ksize=3)

        # Combine the results from the x and y directions
        sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

        # Flipping the image so that kivy displays it correctly
        image = cv2.flip(sobel, 0)

        return np.array(image)
