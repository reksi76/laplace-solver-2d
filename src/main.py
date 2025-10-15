import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from boundary import set_plate_bc
from solver import laplace_jacobi
from visualize import plot_heatmap

nx, ny = 50, 50
phi = set_plate_bc(nx, ny)
it, phi = laplace_jacobi(phi)

print(f'Convergen in {it}')
plot_heatmap(phi)



