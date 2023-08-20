"""
Roberts Cross Edge Detection
"""
import cv2
import numpy as np


class RobertsCrossEdgeDetection:

    def __init__(self, image):
        self.image = image
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def edge(self):
        kernelx = np.array([[1, 0], [0, -1]])
        kernely = np.array([[0, 1], [-1, 0]])
        roberts_x = cv2.filter2D(self.gray_image, -1, kernelx)
        roberts_y = cv2.filter2D(self.gray_image, -1, kernely)
        roberts = roberts_x ** 2 + roberts_y ** 2

        # # Flipping the image so that kivy displays it correctly
        image = cv2.flip(roberts, 0)

        return np.array(image)
