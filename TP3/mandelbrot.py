import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Calculate whether a point is in the Mandelbrot set.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Generate a Mandelbrot fractal image as a 2D NumPy array.
    """
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    fractal = np.zeros((height, width))

    for i, im in enumerate(imag):
        for j, re in enumerate(real):
            fractal[i, j] = mandelbrot(complex(re, im), max_iter)
    return fractal

def plot_fractal(fractal, extent):
    """
    Plot the fractal using Matplotlib.
    """
    plt.imshow(fractal, extent=extent, cmap='inferno')
    plt.colorbar(label="Iterations")
    plt.title("Fractal of Mandelbrot Set")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.show()

xmin, xmax, ymin, ymax = -2.0, 2.0, -2.0, 2.0
width, height = 800, 800
max_iter = 100

fractal = generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)
plot_fractal(fractal, extent=[xmin, xmax, ymin, ymax])
