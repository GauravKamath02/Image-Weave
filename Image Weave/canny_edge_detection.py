"""
using cannny to detect the edges
"""
import cv2
import numpy as np


class CannyEdgeDetection:

    def __init__(self, image):
        self.image = image
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def edge(self):

        # Perform Gaussian blurring to reduce noise
        blurred = cv2.GaussianBlur(self.gray, (3, 3), 0)

        # Perform Canny edge detection with threshold values of 100 and 200
        edges = cv2.Canny(blurred, 100, 200)

        # Flipping the image so kivy displays it correctly
        edges = cv2.flip(edges, 0)
        return edges

