import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
import numpy as np 
from boundary import set_plate_bc
from visualize import plot_heatmap, plot_quiver, animate_solution 
from solver import laplace_jacobi, laplace_gauss_seidle

parser = argparse.ArgumentParser(description='2D Laplace Equation Solver')
parser.add_argument('--solver', choices=['jacobi', 'gauss'], default='gauss', help='choose a solver method (gauss or jacobi)')
parser.add_argument('--nx', type=int, default=50, help='Number of grid x')
parser.add_argument('--ny', type=int, default=50, help='Number of grid y')

args = parser.parse_args()
phi = set_plate_bc(args.nx, args.ny)

if args.solver == 'jacobi':
    it, phi = laplace_jacobi(phi)
if args.solver == 'gauss':
    it,phi, history = laplace_gauss_seidle(phi)

print(f'Convergent in {it} iterations')
plot_heatmap(phi)
plot_quiver(phi)
animate_solution(history)

