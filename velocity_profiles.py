import numpy as npfrom constants import *
from density_profiles import *

def star_disp(radii):
    return np.where(radii < 1, 8.0, np.where(radii > 7, 1.0, 8.0 - (8.0 - 1.0) * ((radii - 1.0) / (7.0 - 1.0))))

def gas_disp(radii):
    return np.where(radii < 13, 5.0, np.where(radii > 15, 0, -2.5*radii + 37.5))

