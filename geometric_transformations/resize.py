import cv2

img = cv2.imread('./images/input.jpg')

img_scaled_linear = cv2.resize(
    img,  # Image
    None,  # Targeted size (here not defined)
    fx=1.2, fy=1.2,  # Scale factors over axes
    interpolation=cv2.INTER_LINEAR,  # interpolation method
)

img_scaled_cubic = cv2.resize(
    img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC
)

img_scaled_skewed = cv2.resize(
    img, (450, 400), interpolation=cv2.INTER_AREA
)

cv2.imshow('Scaling - Linear', img_scaled_linear)
cv2.imshow('Scaling - Cubic', img_scaled_cubic)
cv2.imshow('Scaling - Skewed Size', img_scaled_skewed)

cv2.waitKey()
