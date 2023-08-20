import numpy as np
import matplotlib.pyplot as plt
from p2ic.constants import *

def random_points(N, R_max):
    u = np.random.uniform(0, 1, N)
    v = np.random.uniform(0, 1, N)
    phi = 2 * np.pi * u
    R = R_max * np.sqrt(v)
    return R, phi

def radial_distance(x, y):
    return np.sqrt(x**2 + y**2)

def inter_prof(xlims, ylims, logx=False, logy=False, npts=20, old_prof = None):
    """
    Interactively select data points on a plot

    Parameters:
        xlims (list): List of x-axis limits [xmin, xmax]
        ylims (list): List of y-axis limits [ymin, ymax]

    Returns:
        tuple: Lists of selected x and y coordinates
    """
    ax = plt.gca()
    if old_prof: ax.scatter(old_prof[0], old_prof[1], c='k')
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])
    if logx: ax.set_xscale('log')
    if logy: ax.set_yscale('log')
    pts = plt.ginput(npts)
    plt.close()
    x1 = [p[0] for p in pts]
    y1 = [p[1] for p in pts]

    return x1, y1

