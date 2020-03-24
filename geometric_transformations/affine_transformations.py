# Transformation that preserves points, straiht lines and planes.
#
# Defined as a mapping of three points of the source to 3 destination points

import cv2
import numpy as np

img = cv2.imread('./images/input.jpg')
rows, cols = img.shape[:2]
src_points = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
])  # control points: top corners and bottom left corner

dst_points = np.float32([
    [0, 0],
    [int(0.6 * (cols - 1)), 0],
    [int(0.4 * (cols - 1)), rows - 1],
])  # points to map the controls: top left corner and two points over the top and bottom borders

affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matrix, (cols, rows))

cv2.imshow('Input', img)
cv2.imshow('Output', img_output)
cv2.waitKey()
