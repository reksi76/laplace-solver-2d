import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.solver import laplace_gauss_seidle
from src.boundary import set_plate_bc
from src.visualize import plot_heatmap

nx, ny = 50, 50
phi = set_plate_bc(nx,ny)
it, phi = laplace_gauss_seidle(phi)

print(f'Convergent in {it}')
plot_heatmap(phi)
