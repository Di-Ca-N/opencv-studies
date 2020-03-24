import cv2
import numpy as np

img = cv2.imread('./images/input.jpg')
num_rows, num_cols = img.shape[:2]

# On image translations, the transformation matrix has this format:
#
# 1 0 t_x
# 0 1 t_y
#
# Where t_x and t_y are the values of x and y for with the image will be moved.
# In this example, it is moved by 70 units in x axe (to rigth) and 110 units in y axe (to down)
translation_matrix = np.float32([
    [1, 0, 70],
    [0, 1, 110]
])

# warpAffine apply a matrix transformation to an image
img_translation = cv2.warpAffine(
    img,  # image to transform
    translation_matrix,  # transformation matrix
    (num_cols, num_rows),  # resulting image cols and rows
    cv2.INTER_LINEAR,  # interpolation method

    # next arguments used to fill the borders
    cv2.BORDER_WRAP,
    cv2.BORDER_REPLICATE
)

# This strategy can be used to center an image inside a frame

# img_translation = cv2.warpAffine(
#     img,
#     np.float32([[1, 0, 70], [0, 1, 110]]),
#     (num_cols + 70, num_rows + 110)
# )

# img_translation = cv2.warpAffine(
#     img_translation,  # image
#     np.float32([[1, 0, -30], [0, 1, -50]]),  # transformation matrix

#     # cols and rows of produced image
#     (num_cols + 70 + 30, num_rows + 110 + 50),
# )


cv2.imshow('Translation', img_translation)
cv2.waitKey()
