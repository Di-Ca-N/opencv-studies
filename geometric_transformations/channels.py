import cv2

img = cv2.imread('./images/input.jpg', cv2.IMREAD_COLOR)
g, b, r = cv2.split(img)

# Original image (merging all original channels)
gbr_image = cv2.merge((g, b, r))
cv2.imshow('GBR', gbr_image)

# Two red channels and no green
rbr_image = cv2.merge((r, b, r))
cv2.imshow('RBR', rbr_image)
cv2.waitKey()
