import cv2
import numpy as np

if __name__ == "__main__":
    winname1 = "ORIGINAL"
    img = cv2.imread('sky.jpg', cv2.IMREAD_COLOR)

    try:
        cv2.namedWindow(winname1)
        cv2.moveWindow(winname1, 0, 0)
        cv2.imshow(winname1, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print("Error: Could not load image. Please check the file path and name.")
