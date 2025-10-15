import matplotlib.pyplot as plt 
import numpy as np 
from src.fields import compute_electric_field

def plot_heatmap(phi):
    plt.imshow(phi, origin='lower', cmap='hot')
    plt.colorbar(label='Tempetature')
    plt.title('Laplace Equation Solution (2D)')
    plt.show()

def plot_quiver(phi):
    Ex, Ey = compute_electric_field(phi)
    x = np.arange(1, phi.shape[0]-1)
    y = np.arange(1, phi.shape[1]-1)
    X, Y = np.meshgrid(x,y, indexing='ij')
    plt.imshow(phi, origin='lower', cmap='hot')
    plt.quiver(Y, X, Ex, Ey, color='white')
    plt.title('Electric Field from Potential')
    plt.show()

