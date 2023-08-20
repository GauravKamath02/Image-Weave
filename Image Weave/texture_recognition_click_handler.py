import cv2
import multiprocessing as mp

from local_binary_patterns_texture import LocalBinaryPatternsTexture
from histogram_equiliztion import HistogramEquilization
from gabor_filter_texture import GaborFilterTexture
from contrast_limited_adaptive_histogram_enhancement import ContrastLimitedAdaptiveHistogramEnhancement
from decorrelation_stretch_enhancement import DecorrelationStretchEnhancement


class TextureRecognitionClickHandler:

    def __init__(self, path):
        self.image = cv2.imread(path)

    def menu_option_selected_create_thread(self, operation):
        pool = mp.Pool(processes=mp.cpu_count())
        if operation == "LBP":
            processed_image = pool.apply(self.local_binary_patterns_texture)
        elif operation == "GLCM":
            processed_image = pool.apply(self.histogram_equilization_enhancement)
        elif operation == "Gabor":
            processed_image = pool.apply(self.gabor_filter_texture)
        elif operation == "LTP":
            processed_image = pool.apply(self.contrast_limited_adaptive_histogram)
        elif operation == "SIFT":
            processed_image = pool.apply(self.decorrelation_stretch_enhancement)
        pool.close()
        return processed_image

    def local_binary_patterns_texture(self):
        texture_instance = LocalBinaryPatternsTexture(image=self.image)
        texture = texture_instance.detect()
        return texture

    def histogram_equilization_enhancement(self):
        enhanced_image_instance = HistogramEquilization(image=self.image)
        enhanced_image = enhanced_image_instance.enhance()
        return enhanced_image

    def gabor_filter_texture(self):
        texture_instance = GaborFilterTexture(image=self.image)
        texture = texture_instance.detect()
        return texture

    def contrast_limited_adaptive_histogram(self):
        enhanced_image_instance = ContrastLimitedAdaptiveHistogramEnhancement(image=self.image)
        enhanced_image = enhanced_image_instance.enhance()
        return enhanced_image

    def decorrelation_stretch_enhancement(self):
        enhanced_image_instance = DecorrelationStretchEnhancement(image=self.image)
        enhanced_image = enhanced_image_instance.enhance()
        return enhanced_image
