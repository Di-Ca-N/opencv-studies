import cv2
import numpy as np

shapes_img = cv2.imread('./images/shapes.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = shapes_img.shape

sobel_horizontal = cv2.Sobel(shapes_img, -1, 1, 0, ksize=3)
sobel_vertical = cv2.Sobel(shapes_img, -1, 0, 1, ksize=3)
laplacian = cv2.Laplacian(shapes_img, cv2.CV_64F)

cv2.imshow('Original', shapes_img)
cv2.imshow('Horizontal Sobel', sobel_horizontal)
cv2.imshow('Vertical Sobel', sobel_vertical)
cv2.imshow('Laplacian', laplacian)

cube_img = cv2.imread('./images/cube.jpg', cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(cube_img, cv2.CV_64F)
canny = cv2.Canny(cube_img, 50, 97)

cv2.imshow('Cube Original', cube_img)
cv2.imshow('Cube Laplacian', laplacian)
cv2.imshow('Cube Canny', canny)
cv2.waitKey()
