import numpy as np

# Constants
G = 4.30091e-6  # gravitational constant, (km/s)^2 kpc / (Msol)
rho_crit = 1.27e-7  # critical density, Msol / kpc^3

# Disk properties
m_disk = 1e10  # disk mass, Msol
r_disk = 1  # disk radius, kpc
h_disk = 0.5  # disk scale height, kpc

# Halo properties
m_halo = 1e10  # halo mass, Msol
c = 10  # concentration parameter, dimensionless
a = 5

# Star properties
m_star = 1.3e8  # stellar disk mass, Msol

# Particle properties
m_particle = 10**5  # sim particle mass, Msol
