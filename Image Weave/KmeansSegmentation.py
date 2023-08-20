"""
Performs segmentation Using the k means algorithm
Initialize the class with the image and K value and invoke the segment function.
Source : k-Means Segmentation | Image Segmentation by First Principles of Computer Vision (https://www.youtube.com/watch?v=22mpExWh1LY)
         K-Means Clustering OpenCv (https://docs.opencv.org/4.x/d1/d5c/tutorial_py_kmeans_opencv.html)
"""
import cv2
import numpy as np


class KMeansSegmentation:

    def __init__(self, image, k=4, max_iterations=1000):
        """
        :param image:  =The input image to be segmented
        :param k: The number of clusters
        :param max_iterations: The max number iterations before the algorithm terminates
        """
        self.image = image
        self.k = k
        self.maxIterations = max_iterations

    def segment(self):
        # Reshaping the image into a 2D array of pixels and 3 color values (RGB)
        pixel_values = self.image.reshape((-1, 3))

        # Convert to float type
        pixel_values = np.float32(pixel_values)

        # Determining the criteria function with max number of iterations and required accuracy
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, self.maxIterations, 1)

        # Performing K means
        retval, labels, centers = cv2.kmeans(pixel_values, self.k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        segmented_data = centers[labels.flatten()]
        segmented_image = segmented_data.reshape(self.image.shape)

        # Flipping the image so that kivy displays it correctly
        segmented_image = cv2.flip(segmented_image, 0)

        return segmented_image

