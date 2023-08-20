"""
Performs segmentation based a threshold, mean in this case all values above mean assigned 1 and other 0
Initialize the class with the image to be segmented and invoke the segment Function.
Source : https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
"""
import cv2
import numpy as np


class ThresholdSegmentation:

    def __init__(self, image, **kwargs):
        self.image = image
        self.grayScaledImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def segment(self):
        _, segmented_image = cv2.threshold(self.grayScaledImage, np.mean(self.grayScaledImage), 255,
                                          cv2.THRESH_BINARY_INV)

        # Flipping the image so that kivy displays it correctly
        segmented_image = cv2.flip(segmented_image, 0)

        return segmented_image
