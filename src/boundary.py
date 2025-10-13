import numpy as np 

def set_plate_bc(nx, ny):
    phi = np.zeros((nx, ny))
    phi[-1,:] = 100.0
    return phi
