"""
Contrast-limited adaptive histogram equalization (CLAHE) on an image
"""
import cv2


class ContrastLimitedAdaptiveHistogramEnhancement:

    def __init__(self, image):
        self.image = image
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def enhance(self):
        # Create a CLAHE object with default parameters
        clahe = cv2.createCLAHE()

        # Apply CLAHE to the image
        img_clahe = clahe.apply(self.gray)

        # Flipping the image so kivy displays it correctly
        image = cv2.flip(img_clahe, 0)

        return image
