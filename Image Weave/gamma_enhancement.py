"""
using Gamma Enhancement to enhance the contrast of images
"""
import cv2


class GammaEnhancement:

    def __init__(self, image, gamma=1.5):
        self.image = image
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.gamma = gamma

    def enhance(self):
        # Perform gamma enhancement on the image
        gamma_img = cv2.pow(self.gray / 255.0, self.gamma)
        gamma_img = cv2.normalize(gamma_img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        image = cv2.flip(gamma_img, 0)

        return image



