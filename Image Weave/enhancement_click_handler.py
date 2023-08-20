import cv2
import multiprocessing as mp

from gamma_enhancement import GammaEnhancement
from histogram_equiliztion import HistogramEquilization
from wiener_filter_enhancement import WienerFilterEnhancement
from contrast_limited_adaptive_histogram_enhancement import ContrastLimitedAdaptiveHistogramEnhancement
from decorrelation_stretch_enhancement import DecorrelationStretchEnhancement


class EnhancementClickHandler:

    def __init__(self, path):
        self.image = cv2.imread(path)

    def menu_option_selected_create_thread(self, operation):
        pool = mp.Pool(processes=mp.cpu_count())
        if operation == "Gamma":
            processed_image = pool.apply(self.gamma_enhancement)
        elif operation == "Histogram Equalization":
            processed_image = pool.apply(self.histogram_equilization_enhancement)
        elif operation == "Wiener":
            processed_image = pool.apply(self.wiener_filter_enhancement)
        elif operation == "CLAHE":
            processed_image = pool.apply(self.contrast_limited_adaptive_histogram)
        # elif operation == "Decorrelation Stretch":
        #     processed_image = pool.apply(self.decorrelation_stretch_enhancement)
        pool.close()
        return processed_image

    def gamma_enhancement(self):
        enhanced_image_instance = GammaEnhancement(image=self.image)
        enhanced_image = enhanced_image_instance.enhance()
        return enhanced_image

    def histogram_equilization_enhancement(self):
        enhanced_image_instance = HistogramEquilization(image=self.image)
        enhanced_image = enhanced_image_instance.enhance()
        return enhanced_image

    def wiener_filter_enhancement(self):
        enhanced_image_instance = WienerFilterEnhancement(image=self.image)
        enhanced_image = enhanced_image_instance.enhance()
        return enhanced_image

    def contrast_limited_adaptive_histogram(self):
        enhanced_image_instance = ContrastLimitedAdaptiveHistogramEnhancement(image=self.image)
        enhanced_image = enhanced_image_instance.enhance()
        return enhanced_image

    def decorrelation_stretch_enhancement(self):
        enhanced_image_instance = DecorrelationStretchEnhancement(image=self.image)
        enhanced_image = enhanced_image_instance.enhance()
        return enhanced_image


