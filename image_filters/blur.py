# Low frequency filter

import cv2
import numpy as np

img = cv2.imread('./images/subway.jpg')
rows, cols = img.shape[:2]

# a kernel that consider only the value of the pixel being processed
kernel_identity = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
])
# Divisions to normalize the kernel, that is, make it sum 1, to not increase artificially the intensity of pixels
kernel_3x3 = np.ones((3, 3), np.float32) / 9
kernel_5x5 = np.ones((5, 5), np.float32) / 25

# Applying filters
# -1 to maintain source image depth
output_identity = cv2.filter2D(img, -1, kernel_identity)
output_3x3 = cv2.filter2D(img, -1, kernel_3x3)
output_5x5 = cv2.filter2D(img, -1, kernel_5x5)

cv2.imshow('Original', img)
cv2.imshow('Identity filter', output_identity)
cv2.imshow('3x3 filter', output_3x3)
cv2.imshow('5x5 filter', output_5x5)


# Shortcut to apply blur without having to generate the kernels
output_3x3_auto = cv2.blur(img, (3, 3))
cv2.imshow('Auto 3x3 filter', output_3x3_auto)

cv2.waitKey()
