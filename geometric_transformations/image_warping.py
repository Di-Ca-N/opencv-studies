# Absolutely free transformation

import cv2
import numpy as np
import math

img = cv2.imread('./images/input.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

img_output = np.zeros(img.shape, dtype=img.dtype)

for i in range(rows):
    for j in range(cols):
        offset_x = int(25 * math.sin(2 * math.pi * i / 180))

        if j + offset_x < cols:
            img_output[i, j] = img[i, j + offset_x]
        else:
            img_output[i, j] = 0

cv2.imshow('Vertical wave', img_output)

img_output = np.zeros(img.shape, dtype=img.dtype)

for i in range(rows):
    for j in range(cols):
        offset_y = int(16 * math.sin(2 * math.pi * j / 180))

        if i + offset_y < rows:
            img_output[i, j] = img[(i + offset_y) % rows, j]
        else:
            img_output[i, j] = 0

cv2.imshow('Horizontal wave', img_output)

img_output = np.zeros(img.shape, dtype=img.dtype)

for i in range(rows):
    for j in range(cols):
        offset_x = int(20 * math.sin(2 * math.pi * i / 180))
        offset_y = int(20 * math.sin(2 * math.pi * j / 180))

        img_output[i, j] = img[(i + offset_y) % rows, (j + offset_x) % cols]

cv2.imshow('Bidirectional wave', img_output)


img_output = np.zeros(img.shape, dtype=img.dtype)

for i in range(rows):
    for j in range(cols):
        offset_x = int(128 * math.sin(2 * math.pi * i / cols))
        img_output[i, j] = img[i, (j + offset_x) % cols]

cv2.imshow('Concave', img_output)

cv2.waitKey()
