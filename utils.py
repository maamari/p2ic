import numpy as np
from constants import *

# Function to generate random points
def random_points(N, R_max):
    u = np.random.uniform(0, 1, N)
    v = np.random.uniform(0, 1, N)
    phi = 2 * np.pi * u
    R = R_max * np.sqrt(v)
    return R, phi

# Function to calculate radial distance
def radial_distance(x, y):
    return np.sqrt(x**2 + y**2)
