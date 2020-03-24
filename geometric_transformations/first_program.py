import cv2

# Loads image (stored as a numpy matrix)
img = cv2.imread('./images/input.jpg', cv2.IMREAD_COLOR)

# Convert image to gray colorspace
# gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Convert image to YUV colorspace
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# Shows image
cv2.imshow('Input image', yuv_img)

# Split channels
# y, u, v = cv2.split(yuv_img)
# cv2.imshow('Y Channel', y)
# cv2.imshow('U Channel', u)
# cv2.imshow('V Channel', v)

# Other alternative (Faster)
# cv2.imshow('Y Channel', yuv_image[:, :, 0])
# cv2.imshow('U Channel', yuv_image[:, :, 1])
# cv2.imshow('V Channel', yuv_image[:, :, 2])

# Outputs to file
# cv2.imwrite('images/output.jpg', img)

cv2.waitKey()
