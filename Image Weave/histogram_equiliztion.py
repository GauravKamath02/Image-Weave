"""
using histogram equilization to enhance the contrast of images
"""
import cv2


class HistogramEquilization:

    def __init__(self, image):
        self.image = image
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def enhance(self):
        # Perform contrast enhancement using histogram equalization
        img_eq = cv2.equalizeHist(self.gray)
        image = cv2.flip(img_eq, 0)

        return image
