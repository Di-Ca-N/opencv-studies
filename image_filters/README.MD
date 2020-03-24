# Image Filter

Generally, apply a filter to an image means apply some operation for each pixel of it using a kernel. A kernel is a matrix that, centered on the pixel that is being operated, multiplies every pixel superposed by it and the sum of all entries is the new value of the pixel.

To understand filters, is good to know about frequency in images. The frequency is how fast pixels change on an image. Fast changes means high frequency. With it, low frequency filters tend to smooth the image, while high frequency to sharpen.
