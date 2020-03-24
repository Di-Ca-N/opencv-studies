import cv2
import numpy as np


def print_instructions():
    print("Change cartoonizing mode:\n  1.Without color: press 's'\n 2.With color: press 'c'")


def cartoonize_image(img, ksize=5, sketch_mode=False):
    num_repetitions, sigma_color, sigma_space, ds_factor = 10, 5, 7, 4

    # Convert image to grayscale and smooth some outlier pixels
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 7)

    # Find edges using Laplacian algorithm
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=ksize)

    # threshold to turn all thigs into black and white (everything > than 100 turns
    # into white, due to Binary inverse mode)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    if sketch_mode:
        img_sketch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        kernel = np.ones((3, 3), np.uint8)
        # increasing thickness of lines. Eroded used because we want to increase the black area, so must erode the white one
        img_eroded = cv2.erode(img_sketch, kernel, iterations=1)

        # median blur to enhance quality
        return cv2.medianBlur(img_eroded, ksize=5)

    scale_factor = 1 / ds_factor

    # Reducing size for faster processing
    img_small = cv2.resize(img, None, fx=scale_factor,
                           fy=scale_factor, interpolation=cv2.INTER_AREA)

    for i in range(num_repetitions):
        # Smooths image, keeping the edges
        img_small = cv2.bilateralFilter(
            img_small, ksize, sigma_color, sigma_space
        )

    img_output = cv2.resize(img_small, None, fx=ds_factor,
                            fy=ds_factor, interpolation=cv2.INTER_LINEAR)

    dst = np.zeros(img_gray.shape)
    dst = cv2.bitwise_and(img_output, img_output, mask=mask)
    return dst


if __name__ == "__main__":
    print_instructions()
    cap = cv2.VideoCapture(0)

    cur_mode = None
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=1, fy=1,
                           interpolation=cv2.INTER_AREA)

        c = cv2.waitKey(1)

        if c == 27:
            break

        if c not in (-1, -255, cur_mode):
            cur_mode = c

        if cur_mode == ord('s'):
            cv2.imshow('Cartoonize', cartoonize_image(frame, sketch_mode=True))
        elif cur_mode == ord('c'):
            cv2.imshow('Cartoonize', cartoonize_image(frame))
        else:
            cv2.imshow('Cartoonize', frame)

    cap.release()
    cv2.destroyAllWindows()
