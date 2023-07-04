import numpy as np
from constants import *
from density_profiles import *

def random_points_in_volume(radius, count, is_disk=False):
    """
    Generate random points in a volume.

    Parameters:
        radius (float): Radius of the volume.
        count (int): Number of points to generate.
        is_disk (bool, optional): Whether the volume is a disk. Defaults to False.

    Returns:
        tuple: x, y, and z coordinates of the generated points.
    """
    u = np.random.uniform(0, 1, count)
    v = np.random.uniform(0, 1, count)
    if is_disk:
        theta = 2 * np.pi * u
        r = np.sqrt(-2 * r_disk**2 * np.log(1 - v))
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        z = np.random.normal(0, h_disk, count)
    else:  # is a sphere
        phi = np.arccos(2 * v - 1)
        theta = 2 * np.pi * u
        x = radius * np.sin(phi) * np.cos(theta)
        y = radius * np.sin(phi) * np.sin(theta)
        z = radius * np.cos(phi)
    return x, y, z

def radial_distance(x, y):
    """
    Calculate the radial distance from the origin for given x and y coordinates.

    Parameters:
        x (array-like): x coordinates.
        y (array-like): y coordinates.

    Returns:
        array-like: Radial distances.
    """
    return np.sqrt(x**2 + y**2)

def num_part(radii, profile, m_particle, is_disk=False):
    """
    Calculate the number of particles in a given profile.

    Parameters:
        profile (array-like): Profile values.
        m_particle (float): Mass of each particle.
        is_disk (bool, optional): Whether the profile represents a disk. Defaults to False.

    Returns:
        array-like: Number of particles in the profile.
    """
    if is_disk:
        return profile * np.pi * (radii**2) * h_disk / m_particle
    else:  # is a sphere
        return profile * (4/3) * np.pi * (radii**3) / m_particle

def part_positions(radii, counts, is_disk=False):
    """
    Generate particle positions for each radius.

    Parameters:
        radii (array-like): Array of radii.
        counts (array-like): Array of particle counts for each radius.
        is_disk (bool, optional): Whether the particles belong to a disk. Defaults to False.

    Returns:
        tuple: Arrays of x, y, and z coordinates for the generated particles.
    """
    x, y, z = [], [], []
    for r, count in zip(radii, counts):
        x_r, y_r, z_r = random_points_in_volume(r, int(count), is_disk)
        x.extend(x_r)
        y.extend(y_r)
        z.extend(z_r)

    return np.array(x), np.array(y), np.array(z)

def compute_dens(radii, x, y, z, is_disk=False):
    """
    Compute the density profile based on the particle positions.

    Parameters:
        x (array-like): x coordinates of the particles.
        y (array-like): y coordinates of the particles.
        z (array-like): z coordinates of the particles.
        is_disk (bool, optional): Whether the particles belong to a disk. Defaults to False.

    Returns:
        array-like: Density profile.
    """
    distances = radial_distance(x, y)

    hist, bin_edges = np.histogram(distances, bins=np.append(radii, np.inf), density=False)

    if is_disk:
        areas = np.pi * radii**2
    else:
        volumes = 4/3 * np.pi * radii**3

    masses = hist * m_particle

    if is_disk:
        return masses / areas / h_disk
    else:
        return masses / volumes

