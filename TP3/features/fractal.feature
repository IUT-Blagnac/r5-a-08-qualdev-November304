Feature: Fractal Generation
  To visualize fascinating mathematical patterns
  As a user
  I want to generate and validate the fractals

  Scenario: Generating and validating the Mandelbrot fractal
    Given the following parameters for Mandelbrot:
      | xmin   | xmax   | ymin   | ymax   | width | height | max_iter |
      | -2.0   | 2.0    | -2.0   | 2.0    | 800   | 800    | 100      |
    When I generate the mandelbrot fractal
    Then the image must contain at least one value representing the Mandelbrot set
    And the image must contain regions outside the Mandelbrot set
    And the fractal must have dimensions "800x800"

  Scenario: Generating and validating the Julia fractal
    Given the following parameters for Julia:
      | xmin   | xmax   | ymin   | ymax   | width | height | max_iter | c_real | c_imag |
      | -2.0   | 2.0    | -2.0   | 2.0    | 800   | 800    | 100      | 0.285  | 0.01   |
    When I generate the julia fractal
    Then the image must contain at least one value representing the Julia set
    And the image must contain regions outside the Julia set
    And the fractal must have dimensions "800x800"