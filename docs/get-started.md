
# Get Started

Here we will see how we can make a Mandelbrot set plot with python code.

> [!IMPORTANT] This exercise focuses on intermediate level python users who feel comfortable wiht using numpy and complex numbers

## MandelBrot set

The Mandelbrot set is a beautiful fractal and is defined as the set of complex numbers {math}`c` for which the sequence {math}`z_{n+1} = z_n^2 + c` does not diverge when iterated from {math}`z=0`, i.e., for which the sequence {math}`|z_n|` remains bounded in value.

![Mandelbrot set](./_static/get-started/mandel1s.jpg)

## Code Example

```{literalinclude} ../src/mandelbrot.py
    :language: python
```

## Code Explanation

.. autofunction:: mandelbrot.mandelbrot_set

The mandelbrot.py file contains three functions and an example usage:

:func:`src.mandelbrot.mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)`
:func:`mandelbrot.mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)`
:func:`mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)`

This function generates a 2D array of pixels representing the Mandelbrot set. It takes the minimum and maximum values of the real and imaginary axes (xmin, xmax, ymin, ymax), the width and height of the image (width, height), and the maximum number of iterations (max_iter) as input. It returns three arrays: x, y, and pixels. The x and y arrays contain the real and imaginary values of each pixel, respectively, and the pixels array contains the number of iterations required for each pixel to escape the Mandelbrot set.