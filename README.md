# ComplexPlotter
A tool for displaying the plot of a function with a complex output, taken and extended from QuickRecon/PythonExperiments.

It produces two types of graph, a 2d plot of f(x) with x being represented as a colour gradient and a 3d plot of f(x) with x being the z direction. This is useful in the visualisation of functions that cannot just be plotted on a cartesian plane, such as i^x.

## Help text:

```
usage: complexplotter.py [-h] [--resolution RESOLUTION] Function Minimum Maximum

positional arguments:
  Function              The function to plot in terms of x. Numpy is available
                        with the name np. eg 'np.exp(1j*x)'.
  Minimum               The minimum x value to use.
  Maximum               The maximum x value to use.

optional arguments:
  -h, --help            show this help message and exit
  --resolution RESOLUTION
                        Set the amount of points to sample, default is 10
                        times the difference between Maximum and Minimum.
```

## Usage Examples (all done with reasonable bounds and a resolution of 1000):

e^ix: 
```python complexplotter.py 'np.exp(1j*x)' 0 np.pi --resolution 1000```

i^ix:
```python complexplotter.py 'np.power(1j,1j*x)' 0 2 --resolution 1000```

i^x:
```python complexplotter.py 'np.power(1j,x)' 0 2 --resolution 1000```

x^2 + ix + 3: ```python complexplotter.py 'x**2 + 1j*x + 3' -10 10 --resolution 1000```



