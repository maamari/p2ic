import numpy as np
from constants import *

# Function for MP22 projected stellar surface mass density profile
def surface_density_stars(R):
    Rd = 1.79  # kpc
    return (m_star / (2 * np.pi * Rd**2) * np.exp(-R / Rd))

# Function for MP22 gas surface density profile
def surface_density_gas(R):
    Sigma0_gas = 3.2/1e-6  # Msol/pc^2
    R1 = 1.11  # kpc
    R2 = 16.5  # kpc
    alpha = 18.04
    return Sigma0_gas * np.exp(-R / R1) * (1 + R / R2)**alpha

# Function for MP22 stellar density profile
def rho_stars(R, z):
    sigma_stars = surface_density_stars(R)  # Surface density at radius R
    return sigma_stars * np.exp(-abs(z) / h_disk) / (2 * h_disk)

# Function for MP22 gas density profile
def rho_gas(R, z):
    sigma_gas = surface_density_gas(R)  # Surface density at radius R
    return sigma_gas * np.exp(-abs(z) / h_disk) / (2 * h_disk)

# Function for disk density profile
def rho_exp(r, z):
    return (m_disk / (4 * np.pi * r_disk**2 * h_disk)) * np.exp(-r / r_disk) * np.exp(-abs(z) / h_disk)

# Function for NFW density profile
def rho_nfw(r):
    x = r / r_s
    return rho_0 / (x * (1 + x)**2)

# Function for Plummer sphere density profile
def rho_plummer(r):
    return (3 * m_halo) / (4 * np.pi * (a**3)) * (1 + (r**2) / (a**2))**(-5/2)

