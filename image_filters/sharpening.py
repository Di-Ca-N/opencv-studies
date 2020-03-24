import cv2
import numpy as np

img = cv2.imread('./images/subway.jpg')
cv2.imshow('Original', img)

kernel_sharpen_1 = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
])  # not normalized because already sum up to one
kernel_sharpen_2 = np.array([
    [1, 1, 1],
    [1, -7, 1],
    [1, 1, 1]
])  # not normalized because already sum up to one

# aproximate gaussian kernel (smooth image while enhancing edges, leading to a more natural result)
kernel_sharpen_3 = np.array([
    [-1, -1, -1, -1, -1],
    [-1, 2, 2, 2, -1],
    [-1, 2, 8, 2, -1],
    [-1, 2, 2, 2, -1],
    [-1, -1, -1, -1, -1]
]) / 8

output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)

cv2.imshow('Sharpening', output_1)
cv2.imshow('Excessive sharpening', output_2)
cv2.imshow('Edge enhancement', output_3)
cv2.waitKey()
