"""
Performs segmentation based on the contours Initially detects the edges using Canny to identify the contours
Initialize the class with the image to be segmented and invoke the segment Function.
Source : https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/
"""
import cv2
import numpy as np


class ContourSegmentation:

    def __init__(self, image):
        self.image = image
        self.grayScaledImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def segment(self):
        _, threshold = cv2.threshold(self.grayScaledImage, np.mean(self.grayScaledImage), 255, cv2.THRESH_BINARY_INV)
        edges_image = cv2.dilate(cv2.Canny(threshold, 0, 255), None)
        contours_image = sorted(cv2.findContours(edges_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2],
                               key=cv2.contourArea)[-1]
        mask_image = np.zeros(self.image.shape, np.uint8)
        masked_image = cv2.drawContours(mask_image, [contours_image], -1, 255, -1)

        # Flipping the image so that kivy displays it correctly
        masked_image = cv2.flip(masked_image, 0)

        return masked_image

