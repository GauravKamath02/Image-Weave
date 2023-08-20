"""
Prewitt Edge Detection
"""
import cv2
import numpy as np


class PrewittEdgeDetection:

    def __init__(self, image):
        self.image = image
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def edge(self):
        # Apply Prewitt edge detection in the x and y directions
        kernelx = cv2.getDerivKernels(1, 0, 3)[0]
        kernely = cv2.getDerivKernels(0, 1, 3)[0]
        prewittx = cv2.filter2D(self.gray_image, -1, kernelx)
        prewitty = cv2.filter2D(self.gray_image, -1, kernely)

        # Combine the results from the x and y directions
        prewitt = cv2.addWeighted(prewittx, 0.5, prewitty, 0.5, 0)

        # Flipping the image so that kivy displays it correctly
        image = cv2.flip(prewitt, 0)

        return np.array(image)
