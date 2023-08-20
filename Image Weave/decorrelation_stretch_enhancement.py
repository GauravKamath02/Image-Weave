"""
performs Decorrelation Stretch on a color image
"""
import cv2
import numpy as np


class DecorrelationStretchEnhancement:

    def __init__(self, image):
        self.image = image

        # Convert the image to Lab color space
        self.img_lab = cv2.cvtColor(self.image, cv2.COLOR_BGR2LAB)

    def enhance(self):
        # Compute the mean and covariance matrices for the a and b channels
        a_mean, a_stddev = cv2.meanStdDev(self.img_lab[:, :, 1])
        b_mean, b_stddev = cv2.meanStdDev(self.img_lab[:, :, 2])
        covariance_matrix = np.cov(self.img_lab[:, :, 1:].reshape(-1, 2).T)

        # Compute the eigenvectors and eigenvalues of the covariance matrix
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

        # Compute the transformation matrix
        transformation_matrix = np.matmul(eigenvectors.T, np.diag(1.0 / np.sqrt(eigenvalues)))

        # Subtract the mean values from the a and b channels
        a_minus_mean = self.img_lab[:, :, 1] - a_mean
        b_minus_mean = self.img_lab[:, :, 2] - b_mean

        # Stack the difference images into a single matrix
        diff_matrix = np.stack((a_minus_mean, b_minus_mean))

        # Compute the stretched image
        stretched_matrix = np.matmul(transformation_matrix, diff_matrix)

        # Reshape the stretched matrix and add the mean values back in
        stretched_a = stretched_matrix[0, :, :] * a_stddev + a_mean
        stretched_b = stretched_matrix[1, :, :] * b_stddev + b_mean
        stretched_ab = np.stack((self.img_lab[:, :, 0], stretched_a, stretched_b), axis=-1)
        stretched_img = cv2.cvtColor(stretched_ab.astype(np.uint8), cv2.COLOR_LAB2BGR)

        image = cv2.flip(stretched_img, 0)

        return image
