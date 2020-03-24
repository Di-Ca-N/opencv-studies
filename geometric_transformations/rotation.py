import cv2
import numpy as np

img = cv2.imread('./images/input.jpg')
num_rows, num_cols = img.shape[:2]

# Rotation is obtained by the following transform matrix
#
# cos\theta -sin\theta
# sin\theta cos\theta
#
# To simplify this, the following function builds this matrix
rotation_matrix = cv2.getRotationMatrix2D(
    (num_cols / 2, num_rows / 2),  # center of rotation
    30,  # angle in degrees
    .7  # scale factor
)

img_rotation = cv2.warpAffine(
    img,
    rotation_matrix,
    (num_cols, num_rows),
)

cv2.imshow('Image Rotation', img_rotation)

# To make the image fit in the frame, we can use the translation function

translation_matrix = np.float32([
    [1, 0, int(.5 * num_cols)],
    [0, 1, int(.5 * num_rows)]
])  # image left upper corner goes to a quarter of height and width

# rotation around the center
rotation_matrix = cv2.getRotationMatrix2D(
    (num_cols, num_rows), 30, 1
)

img_translation = cv2.warpAffine(
    img, translation_matrix, (2 * num_cols, 2 * num_rows)
)
img_rotation_and_translation = cv2.warpAffine(
    img_translation, rotation_matrix, (2 * num_cols, 2 * num_rows)
)

cv2.imshow('Rotation and Translation', img_rotation_and_translation)
cv2.waitKey()
