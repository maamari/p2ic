import numpy as np
from constants import *
from density_profiles import *

def star_disp(radii):
    """
    Calculate the stellar velocity dispersion profile

    Parameters:
        radii (array-like): Array of radii

    Returns:
        array-like: Stellar velocity dispersion at the given radii
    """
    return np.where(radii < 1, 8.0, np.where(radii > 7, 1.0, 8.0 - (8.0 - 1.0) * ((radii - 1.0) / (7.0 - 1.0))))

def gas_disp(radii):
    """
    Calculate the gas velocity dispersion profile

    Parameters:
        radii (array-like): Array of radii

    Returns:
        array-like: Gas velocity dispersion at the given radii
    """
    return np.where(radii < 13, 5.0, np.where(radii > 15, 0, -2.5*radii + 37.5))

