import cv2
from skimage import feature
from skimage.color import gray2rgba


class LocalBinaryPatternsTexture:
    def __init__(self, image):
        self.image = image
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def detect(self):
        # Apply LBP
        lbp = feature.local_binary_pattern(self.gray, 12, 3)
        lbp_image_rgba = gray2rgba(lbp)

        # Flipping the image so kivy displays it correctly
        image = cv2.flip(lbp_image_rgba, 0)

        return image
