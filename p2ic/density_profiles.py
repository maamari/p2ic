import numpy as np
from constants import *

def surface_density_stars(R):
    """
    Calculate the MP22 projected stellar surface mass density profile

    Parameters:
        R (float): Radius

    Returns:
        float: Stellar surface mass density at the given radius
    """
    Rd = 1.79  # kpc
    return (m_star / (2 * np.pi * Rd**2) * np.exp(-R / Rd))

def surface_density_gas(R):
    """
    Calculate the MP22 gas surface density profile

    Parameters:
        R (float): Radius

    Returns:
        float: Gas surface density at the given radius
    """
    Sigma0_gas = 3.2/1e-6  # Msol/pc^2
    R1 = 1.11  # kpc
    R2 = 16.5  # kpc
    alpha = 18.04
    return Sigma0_gas * np.exp(-R / R1) * (1 + R / R2)**alpha

def rho_stars(R, z):
    """
    Calculate the MP22 stellar density profile

    Parameters:
        R (float): Radius
        z (float): Height

    Returns:
        float: Stellar density at the given radius and height
    """
    sigma_stars = surface_density_stars(R)  # Surface density at radius R
    return sigma_stars * np.exp(-abs(z) / h_disk) / (2 * h_disk)

def rho_gas(R, z):
    """
    Calculate the MP22 gas density profile

    Parameters:
        R (float): Radius
        z (float): Height

    Returns:
        float: Gas density at the given radius and height
    """
    sigma_gas = surface_density_gas(R)  # Surface density at radius R
    return sigma_gas * np.exp(-abs(z) / h_disk) / (2 * h_disk)

def rho_exp(r, z):
    """
    Calculate the disk density profile

    Parameters:
        r (float): Radial distance
        z (float): Height

    Returns:
        float: Density at the given radial distance and height
    """
    return (m_disk / (4 * np.pi * r_disk**2 * h_disk)) * np.exp(-r / r_disk) * np.exp(-abs(z) / h_disk)

def rho_nfw(r, r_s, rho_0):
    """
    Calculate the NFW density profile

    Parameters:
        r (float): Radial distance

    Returns:
        float: Density at the given radial distance
    """
    x = r / r_s
    return rho_0 / (x * (1 + x)**2)

def rho_plummer(r):
    """
    Calculate the Plummer sphere density profile

    Parameters:
        r (float): Radial distance

    Returns:
        float: Density at the given radial distance
    """
    return (3 * m_halo) / (4 * np.pi * (a**3)) * (1 + (r**2) / (a**2))**(-5/2)

