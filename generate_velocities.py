# Define the velocity dispersion function
def vdisp_function(radii, existing_radii, existing_dispersions):
    # Create interpolation function
    interp = interp1d(existing_radii, existing_dispersions, kind='linear', fill_value='extrapolate')

    # Calculate interpolated dispersions
    vdisp = interp(radii)
    
    return vdisp

def inter_prof(xlims, ylims):
    %matplotlib

    ax = plt.gca()
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])

    pts = plt.ginput(20)
    plt.close()
    x1 = [p[0] for p in pts]
    y1 = [p[1] for p in pts]
    
    %matplotlib inline
    
    return x1, y1

def dispersion(x, y, z, v_mag, disp_func=None):
    # Calculate radial distance
    radii = np.sqrt(x**2 + y**2 + z**2)

    # Calculate tangential unit vector
    norm = np.sqrt(x**2 + y**2)  # Norm in x-y plane
    ux = -y / norm
    uy = x / norm
    uz = np.zeros_like(z)

    # Calculate velocity dispersion based on radial distance
    if disp_func: disp_func(radii)
    else:
        r, prof = inter_prof([0,20],[0,20])
        vdisp = vdisp_function(radii, r, prof)
    
    # Add velocity dispersion to magnitude
    v_mag_updated = np.random.normal(v_mag, vdisp, len(x))

    # Calculate velocity components
    vx = v_mag_updated * ux
    vy = v_mag_updated * uy
    vz = v_mag_updated * uz

    return radii, vx, vy, vz


