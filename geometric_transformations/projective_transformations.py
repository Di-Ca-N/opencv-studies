# Express the change of point of view of the shape

import cv2
import numpy as np

img = cv2.imread('./images/input.jpg')
rows, cols = img.shape[:2]

src_points_1 = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1],
])
dst_points_1 = np.float32([
    [0, 0],
    [cols - 1, 0],
    [int(.33 * cols), rows - 1],
    [int(.66 * cols), rows - 1],
])
perspective_matrix_1 = cv2.getPerspectiveTransform(src_points_1, dst_points_1)
img_output_1 = cv2.warpPerspective(img, perspective_matrix_1, (cols, rows))

src_points_2 = np.float32([
    [0, 0],
    [0, rows - 1],
    [cols / 2, 0],
    [cols / 2, rows - 1],
])
dst_points_2 = np.float32([
    [0, 100],
    [0, rows - 101],
    [cols / 2, 0],
    [cols / 2, rows - 1]
])
perspective_matrix_2 = cv2.getPerspectiveTransform(src_points_2, dst_points_2)
img_output_2 = cv2.warpPerspective(img, perspective_matrix_2, (cols, rows))

cv2.imshow('Input', img)
cv2.imshow('Output 1', img_output_1)
cv2.imshow('Output 2', img_output_2)
cv2.waitKey()
