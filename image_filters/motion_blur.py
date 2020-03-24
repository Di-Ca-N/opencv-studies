# Motion blur follows the same idea of blur, but apllied to only one direction
# A motion blur kernel would be something like
#
#   0 0 0
#   1 1 1
#   0 0 0

import cv2
import numpy as np

img = cv2.imread('images/subway.jpg')
cv2.imshow('Original', img)

size = 15

# kernel generation
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[(size - 1) // 2, :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size  # normalization

output = cv2.filter2D(img, -1, kernel_motion_blur)
cv2.imshow('Motion blur', output)
cv2.waitKey()
