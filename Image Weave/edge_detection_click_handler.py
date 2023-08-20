import cv2
import multiprocessing as mp

from canny_edge_detection import CannyEdgeDetection
from lapliacian_edge_detection import LapliacianEdgeDetection
from sobel_edge_detection import SobelEdgeDetection
from prewitt_edge_detection import PrewittEdgeDetection
from roberts_cross_edge_detection import RobertsCrossEdgeDetection


class EdgeDetectionClickHandler:

    def __init__(self, path):
        self.image = cv2.imread(path)

    def menu_option_selected_create_thread(self, operation):
        pool = mp.Pool(processes=mp.cpu_count())
        if operation == "Canny":
            processed_image = pool.apply(self.canny_edge)
        elif operation == "Laplician":
            processed_image = pool.apply(self.laplician_edge)
        elif operation == "Sobel":
            processed_image = pool.apply(self.sobel_edge)
        elif operation == "Prewitt":
            processed_image = pool.apply(self.prewitt_edge)
        elif operation == "Robert Cross":
            processed_image = pool.apply(self.robert_cross_edge)
        pool.close()
        return processed_image

    def canny_edge(self):
        edge_image = CannyEdgeDetection(image=self.image)
        edge_detected_image = edge_image.edge()
        return edge_detected_image

    def laplician_edge(self):
        edge_image = LapliacianEdgeDetection(image=self.image)
        edge_detected_image = edge_image.edge()
        return edge_detected_image

    def sobel_edge(self):
        edge_image = SobelEdgeDetection(image=self.image)
        edge_detected_image = edge_image.edge()
        return edge_detected_image

    def prewitt_edge(self):
        edge_image = PrewittEdgeDetection(image=self.image)
        edge_detected_image = edge_image.edge()
        return edge_detected_image

    def robert_cross_edge(self):
        edge_image = RobertsCrossEdgeDetection(image=self.image)
        edge_detected_image = edge_image.edge()
        return edge_detected_image


