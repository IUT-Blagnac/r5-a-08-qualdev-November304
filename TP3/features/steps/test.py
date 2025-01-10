from behave import given, when, then
import numpy as np

# Reutilisable

@given('the following parameters for Mandelbrot')
def step_given_parametersMb(context):
    for row in context.table:
        context.params = {
            "xmin": float(row['xmin']),
            "xmax": float(row['xmax']),
            "ymin": float(row['ymin']),
            "ymax": float(row['ymax']),
            "width": int(row['width']),
            "height": int(row['height']),
            "max_iter": int(row['max_iter'])
        }

@given('the following parameters for Julia')
def step_given_parametersMb(context):
    for row in context.table:
        context.params = {
            "xmin": float(row['xmin']),
            "xmax": float(row['xmax']),
            "ymin": float(row['ymin']),
            "ymax": float(row['ymax']),
            "width": int(row['width']),
            "height": int(row['height']),
            "max_iter": int(row['max_iter']),
            "c_real": float(row['c_real']),
            "c_imag": float(row['c_imag'])
        }

@then('the fractal must have dimensions "{width}x{height}"')
def step_then_check_dimensions(context, width, height):
    expected_width = int(width)
    expected_height = int(height)
    fractal_shape = context.fractal.shape
    assert fractal_shape == (expected_height, expected_width), \
        f"Expected dimensions: {expected_width}x{expected_height}, but got: {fractal_shape}"

# Pr la fractale de mandelbrot

@when('I generate the mandelbrot fractal')
def step_when_generate_fractal(context):
    def mandelbrot(c, max_iter):
        z = 0
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = z**2 + c
        return max_iter

    def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
        real = np.linspace(xmin, xmax, width)
        imag = np.linspace(ymin, ymax, height)
        fractal = np.zeros((height, width))

        for i, im in enumerate(imag):
            for j, re in enumerate(real):
                fractal[i, j] = mandelbrot(complex(re, im), max_iter)
        return fractal

    params = context.params
    context.fractal = generate_fractal(
        params["xmin"], params["xmax"],
        params["ymin"], params["ymax"],
        params["width"], params["height"],
        params["max_iter"]
    )

@then('the image must contain at least one value representing the Mandelbrot set')
def step_then_contains_mandelbrot(context):
    fractal = context.fractal
    max_iter = context.params["max_iter"]
    assert np.any(fractal == max_iter), \
        "No values in the image represent points in the Mandelbrot set."

@then('the image must contain regions outside the Mandelbrot set')
def step_then_contains_outside(context):
    fractal = context.fractal
    max_iter = context.params["max_iter"]
    assert np.any(fractal < max_iter), \
        "No regions outside the Mandelbrot set were found in the image."

# Pr la fractale de julia

@when(u'I generate the julia fractal')
def step_impl(context):
    x = np.linspace(context.params["xmin"], context.params["xmax"], context.params["width"])
    y = np.linspace(context.params["ymin"], context.params["ymax"], context.params["height"])
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y 
    image = np.zeros(Z.shape, dtype=int) 

    c = complex(context.params["c_real"], context.params["c_imag"])

    for i in range(context.params["max_iter"]):
        Z = Z**2 + c 
        mask = np.abs(Z) > 2  
        image[mask] = i 

    context.fractal = image

@then(u'the image must contain at least one value representing the Julia set')
def step_impl(context):
    assert np.any(context.fractal > 0), "L'image ne contient pas de valeurs représentant l'ensemble de Julia"


@then(u'the image must contain regions outside the Julia set')
def step_impl(context):
    assert np.any(context.fractal == 0), "L'image ne contient pas de régions en dehors de l'ensemble de Julia"

