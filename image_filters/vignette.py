import cv2
import numpy as np

img = cv2.imread('./images/cube.jpg')
rows, cols = img.shape[:2]

# Creating gaussian kernel to aplly the effect
kernel_x = cv2.getGaussianKernel(cols, 200)
kernel_y = cv2.getGaussianKernel(rows, 200)
kernel = kernel_y * kernel_x.T

# Kernel to vignette centered not on the center of image.
# Effect achieved by creating a bigger kernel
kernel_x_offset = cv2.getGaussianKernel(int(1.5 * cols), 200)
kernel_y_offset = cv2.getGaussianKernel(int(1.5 * rows), 200)
kernel_offset = kernel_y_offset * kernel_x_offset.T


# Generating mask based on kernel
# Normalized kernel scaled up. The sacling is necessary to avoid that all the image
# remains black (due to value much close to zero) after aplly the mask
mask = 255 * kernel / np.linalg.norm(kernel)

# Creating mask from kernel and, then, taking just the necessary size to fit the image
mask_offset = 255 * kernel_offset / np.linalg.norm(kernel_offset)
mask_offset = mask_offset[int(.5 * rows):, int(.5 * cols):]

output = np.copy(img)
output_offset = np.copy(img)

# Applying mask to each channel of image
for i in range(3):
    output[:, :, i] = output[:, :, i] * mask
    output_offset[:, :, i] = output_offset[:, :, i] * mask_offset

cv2.imshow('Original', img)
cv2.imshow('Vignette 1', output)
cv2.imshow('Vignette 2', output_offset)

cv2.waitKey()
