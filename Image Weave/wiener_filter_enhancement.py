"""
performs image enhancement using a Wiener filter
"""
import cv2


class WienerFilterEnhancement:

    def __init__(self, image):
        self.image = image
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def enhance(self):
        # Perform Wiener filtering to remove the noise and enhance the image
        img_wiener = cv2.fastNlMeansDenoising(self.gray, None, 10, 7, 21)
        image = cv2.flip(img_wiener, 0)

        return image
