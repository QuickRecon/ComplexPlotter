import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mcoll
from mpl_toolkits.mplot3d import Axes3D
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Function", help="The function to plot in terms of x. "
                                     "Numpy is available with the name np. eg 'np.exp(1j*x)'.")
parser.add_argument("Minimum", help="The minimum x value to use.")
parser.add_argument("Maximum", help="The maximum x value to use.")
parser.add_argument("--resolution", help="Set the amount of points to sample, default is 10 times the difference"
                                         " between Maximum and Minimum.")
args = parser.parse_args()

f = lambda x: eval(args.Function)
minimum = eval(args.Minimum)
maximum = eval(args.Maximum)
resolution = (maximum-minimum)*10
if args.resolution:
    resolution = eval(args.resolution)

z = np.linspace(minimum, maximum, resolution)
x = np.real(f(z))
y = np.imag(f(z))

def multicolored_lines():
    """
    http://nbviewer.ipython.org/github/dpsanders/matplotlib-examples/blob/master/colorline.ipynb
    http://matplotlib.org/examples/pylab_examples/multicolored_line.html
    """

    fig, ax = plt.subplots()
    lc = colorline(x, y, z=z, cmap='hsv', norm=plt.Normalize(0.0, z.max()))
    cbar = plt.colorbar(lc)
    cbar.set_label('$x$', rotation=0)
    
    xlim = max(abs(x.min()), abs(x.max()))
    ylim = max(abs(y.min()), abs(y.max()))

    plt.xlim(-(xlim+0.15*xlim), xlim+0.15*xlim)
    plt.ylim(-(ylim+0.15*ylim), ylim+0.15*ylim)

    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")

    ax.grid(color='black', linestyle='-', linewidth=0.5, alpha=0.5)
    plt.axhline(c='black')
    plt.axvline(c='black')
    plt.title("$f(x) = " + args.Function + "$")

    fig2 = plt.figure()
    ax3 = fig2.gca(projection='3d')
    ax3.plot(x, y, z)
    ax3.set_xlabel("Real")
    ax3.set_ylabel("Imaginary")

    x0 = [0] * len(z)
    y0 = [0] * len(z)
    ax3.plot(x0, y0, z, 'k--', alpha=0.8, linewidth=2)
    plt.xlim(-(xlim + 0.15 * xlim), xlim + 0.15 * xlim)
    plt.ylim(-(ylim + 0.15 * ylim), ylim + 0.15 * ylim)
    plt.title("$f(x) = " + args.Function + "$")
    plt.show()


def colorline(x, y, z=None, cmap='copper', norm=plt.Normalize(0.0, 10.0),linewidth=3, alpha=1.0):
    """
    http://nbviewer.ipython.org/github/dpsanders/matplotlib-examples/blob/master/colorline.ipynb
    http://matplotlib.org/examples/pylab_examples/multicolored_line.html
    Plot a colored line with coordinates x and y
    Optionally specify colors in the array z
    Optionally specify a colormap, a norm function and a line width
    """

    # Default colors equally spaced on [0,1]:
    if z is None:
        z =  np.linspace(0.0, 1.0, len(x))

    # Special case if a single number:
    # to check for numerical input -- this is a hack
    if not hasattr(z, "__iter__"):
        z = np.array([z])

    z = np.asarray(z)

    segments = make_segments(x, y)
    lc = mcoll.LineCollection(segments, array=z, cmap=cmap, norm=norm,
                              linewidth=linewidth, alpha=alpha)

    ax = plt.gca()
    ax.add_collection(lc)

    return lc


def make_segments(x, y):
    """
    Create list of line segments from x and y coordinates, in the correct format
    for LineCollection: an array of the form numlines x (points per line) x 2 (x
    and y) array
    """

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments


multicolored_lines()

