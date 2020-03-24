import cv2
import numpy as np

img = cv2.imread('./images/dark.png', cv2.IMREAD_GRAYSCALE)

histeq = cv2.equalizeHist(img)

cv2.imshow('Input', img)
cv2.imshow('Histogram Equalized', histeq)

# In colored images, is possible to equalize the histogram by applying
# the operation only on the Y (Luminance) channel (in YUV)
colored_image = cv2.imread('./images/subway.jpg')
img_yuv = cv2.cvtColor(colored_image, cv2.COLOR_BGR2YUV)
img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Color input', colored_image)
cv2.imshow('Histogram equalized', img_output)
cv2.waitKey()
