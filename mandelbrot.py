import numpy as np
from PIL import Image
import time


def mandelbrot(c, maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return 0


def mandelbrot_set(xmin, xmax, ymin, ymax, img, maxiter):
    width, height = img.size[0], img.size[1]
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)

    [img.putpixel((idx1, idx2),
                  (mandelbrot(complex(r, i), maxiter) << 21) +
                  (mandelbrot(complex(r, i), maxiter) << 10)
                  + mandelbrot(complex(r, i), maxiter) * 8) for idx1, r in enumerate(r1) for idx2, i in enumerate(r2)]


bitmap = Image.new("RGB", (8000, 8000), "white")

start = time.time()
mandelbrot_set(-2.0, 0.5, -1.25, 1.25, bitmap, 100)
print("执行时间 {} 秒".format(round(time.time() - start, 2)))

bitmap.show()
