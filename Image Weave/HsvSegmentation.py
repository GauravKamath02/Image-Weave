"""
Performs segmentation based on (hue, saturation, value)
Initialize the class with the image to be segmented and invoke the segment Function.
Source : https://docs.opencv.org/3.4/df/d9d/tutorial_py_colorspaces.html
"""
import cv2


class HsvSegmentation:

    def __init__(self, image):
        self.image = image

    def segment(self):
        hsv_segmented_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2HSV)

        # Flipping the image in order for kivy to display correctly.
        hsv_segmented_image = cv2.flip(hsv_segmented_image, 0)

        return hsv_segmented_image
