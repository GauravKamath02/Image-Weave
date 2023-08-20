import cv2
import multiprocessing as mp


from MeanShiftSegmentation import MeanShiftSegmentation
from ThresholdSegmentation import ThresholdSegmentation
from KmeansSegmentation import KMeansSegmentation
from ContourSegmentation import ContourSegmentation
from HsvSegmentation import HsvSegmentation


class SegmentationClickHandler:

    def __init__(self, path):
        self.selected_image = cv2.imread(path)  # Image selected by the user

    def menu_option_selected_create_thread(self, operation):
        pool = mp.Pool(processes=mp.cpu_count())
        if operation == "mean_shift_segmentation":
            processed_images = pool.apply(self.mean_shift_segment)
        elif operation == "threshold_segmentation":
            processed_images = pool.apply(self.threshold_segmentation)
        elif operation == "kmeans_segmentation":
            processed_images = pool.apply(self.kmeans_segmentation)
        elif operation == "contour_segmentation":
            processed_images = pool.apply(self.contour_segmentation)
        elif operation == "hsv_segmentation":
            processed_images = pool.apply(self.hsv_segmentation)
        pool.close()
        return processed_images

    def mean_shift_segment(self):
        segment_image = MeanShiftSegmentation(image=self.selected_image)
        segmented_image = segment_image.segment()
        return segmented_image

    def threshold_segmentation(self):
        segment_image = ThresholdSegmentation(image=self.selected_image)
        segmented_image = segment_image.segment()
        return segmented_image

    def kmeans_segmentation(self):
        segment_image = KMeansSegmentation(image=self.selected_image, k=4)
        segmented_image = segment_image.segment()
        return segmented_image

    def contour_segmentation(self):
        segment_image = ContourSegmentation(image=self.selected_image)
        segmented_image = segment_image.segment()
        return segmented_image

    def hsv_segmentation(self):
        segment_image = HsvSegmentation(image=self.selected_image)
        segmented_image = segment_image.segment()
        return segmented_image
