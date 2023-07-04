import numpy as np
from p2ic.constants import *
from p2ic.density_profiles import *
from p2ic.velocity_profiles import *
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def vdisp_function(radii, existing_radii, existing_dispersions):
    """
    Calculate the velocity dispersion based on existing data points

    Parameters:
        radii (array-like): Array of radii to calculate the dispersion for
        existing_radii (array-like): Array of existing radii
        existing_dispersions (array-like): Array of existing velocity dispersions

    Returns:
        array-like: Velocity dispersions at the given radii
    """
    interp = interp1d(existing_radii, existing_dispersions, kind='linear', fill_value='extrapolate')
    vdisp = interp(radii)
    return vdisp

def inter_prof(xlims, ylims):
    """
    Interactively select data points on a plot

    Parameters:
        xlims (list): List of x-axis limits [xmin, xmax]
        ylims (list): List of y-axis limits [ymin, ymax]

    Returns:
        tuple: Lists of selected x and y coordinates
    """
    ax = plt.gca()
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])
    pts = plt.ginput(20)
    plt.close()
    x1 = [p[0] for p in pts]
    y1 = [p[1] for p in pts]
    
    return x1, y1

def dispersion(x, y, z, v_mag, disp_func=None):
    """
    Calculate the dispersion of velocity components

    Parameters:
        x (array-like): x coordinates
        y (array-like): y coordinates
        z (array-like): z coordinates
        v_mag (float): Magnitude of velocity
        disp_func (function, optional): Function to calculate the velocity dispersion. Defaults to None

    Returns:
        tuple: Radial distances and velocity components (vx, vy, vz)
    """
    radii = np.sqrt(x**2 + y**2 + z**2)
    norm = np.sqrt(x**2 + y**2)
    ux = -y / norm
    uy = x / norm
    uz = np.zeros_like(z)
    if disp_func:
        disp_func(radii)
    else:
        r, prof = inter_prof([0,20],[0,20])
        vdisp = vdisp_function(radii, r, prof)
        print(vdisp)
    v_mag_updated = np.random.normal(v_mag, np.abs(vdisp), len(x))
    vx = v_mag_updated * ux
    vy = v_mag_updated * uy
    vz = v_mag_updated * uz
    return radii, vx, vy, vz, r, prof

