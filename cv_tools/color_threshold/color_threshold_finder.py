import cv2
import numpy as np
import os


class ColorThresholdFinder:
    def __init__(
        self,
        image_path: str | None = None,
        image: np.ndarray | None = None,
        display_image: bool = False,
        display_mask: bool = False,
        display_result: bool = True,
        thresholds_path: str = "thresholds.txt",
    ):
        """
        Initialization of the class for selecting color thresholds
        Either image_path or image must be provided
        If both are provided, image_path will be used and image will be ignored

        Args:
            image_path (str): path to the image
            image (np.ndarray): image to be used
            display_image (bool): automatically display the original image
            display_mask (bool): automatically display the mask
            display_result (bool): automatically display the result
            thresholds_path (str): path to the file to save the thresholds
        """

        self.h_min = 0
        self.h_max = 179
        self.s_min = 0
        self.s_max = 255
        self.v_min = 0
        self.v_max = 255
        self.thresholds_path = thresholds_path

        self.image = None
        self.mask = None
        self.result = None

        if image_path is not None:
            self.image = self.load_image(image_path)
        elif image is not None:
            self.image = image
        else:
            raise ValueError("Either image_path or image must be provided")

        self.hsv_image = self.convert_to_hsv(self.image)
        self.display_image = display_image
        self.display_mask = display_mask
        self.display_result = display_result

    def load_image(self, image_path: str):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

        return cv2.imread(image_path)

    def convert_to_hsv(self, image: np.ndarray):
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def create_trackbars(self):
        cv2.namedWindow("Trackbars")
        cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, self.on_trackbar_change)
        cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, self.on_trackbar_change)
        cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, self.on_trackbar_change)
        cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, self.on_trackbar_change)
        cv2.createTrackbar("Val Min", "Trackbars", 0, 255, self.on_trackbar_change)
        cv2.createTrackbar("Val Max", "Trackbars", 255, 255, self.on_trackbar_change)

    def on_trackbar_change(self, x):
        try:
            self.h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
            self.h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
            self.s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
            self.s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
            self.v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
            self.v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
        except cv2.error:
            # Ignore errors during trackbar initialization
            pass

    def show_image(self):
        cv2.imshow("Image", self.image)

    def show_mask(self):
        cv2.imshow("Mask", self.mask)

    def show_result(self):
        cv2.imshow("Result", self.result)

    def find_color_threshold(self):

        self.create_trackbars()

        while True:

            lower_threshold = np.array([self.h_min, self.s_min, self.v_min])
            upper_threshold = np.array([self.h_max, self.s_max, self.v_max])

            if self.display_mask:
                self.mask = cv2.inRange(
                    self.hsv_image, lower_threshold, upper_threshold
                )
                self.show_mask()

            if self.display_result:
                self.result = cv2.bitwise_and(self.image, self.image, mask=self.mask)
                self.show_result()

            if self.display_image:
                self.show_image()

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            if cv2.waitKey(1) & 0xFF == ord("s"):
                self.save_thresholds(lower_threshold, upper_threshold)

    def save_thresholds(self, lower, upper):
        with open(self.thresholds_path, "w") as f:
            f.write(f"Lower: {lower.tolist()}\n")
            f.write(f"Upper: {upper.tolist()}\n")
