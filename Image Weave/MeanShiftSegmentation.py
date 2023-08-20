"""
Performs segmentation Using the k means algorithm
Initialize the class with the image to segment and invoke segment
Source : Mean-Shift Segmentation | Image Segmentation by First Principles of Computer Vision (https://www.youtube.com/watch?v=PCNz_zttmtA)
         estimate_bandwidth scikit learn (https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html)
         Mean shift scikit learn (https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html)
"""
import cv2
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth


class MeanShiftSegmentation:

    def __init__(self, image):
        self.image = image

    def segment(self):
        original_shape = np.shape(self.image)

        # Reshaping the image into a 2D array of pixels and 3 color values (RGB)
        flat_image = np.reshape(self.image, [-1, 3])

        # Estimate bandwidth for mean shift algorithm
        bandwidth = estimate_bandwidth(flat_image, quantile=0.1, n_samples=1000)
        model = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        model.fit(flat_image)
        cluster_centers = model.cluster_centers_
        labels = model.labels_
        segmented_image = cluster_centers[np.reshape(labels, original_shape[:2])]

        # Converting the image to uint8 encoding format
        segmented_image = np.uint8(segmented_image)

        # Flipping the image so that kivy displays it correctly
        segmented_image = cv2.flip(segmented_image, 0)

        return segmented_image

