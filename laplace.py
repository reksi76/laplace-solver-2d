import numpy as np 
import matplotlib.py as plt

N = 50
V0 = 100.0
max_iter = 1000 
tol = 1e-5

phi = np.zeros((N,N))

phi[-1, :] = V0

for it in range(max_iter):
    phi_new = phi.copy()
    for i in range(1, N-1):
        for j in range(1, N-1):
            phi_new[1, j] = 0.25 * (phi[i+1, j] + phi[i-1,j] + phi[i, j+1] + phi[i, j-1])

    diff = np. max(np.abs(phi_new - phi))
    phi = phi_new

    if diff < tol:
        print(f'Konvergen pada iterasi ke-{it}')
        break

plt.imshow(phi, origin='lower', cmap='hot')
plt.colorbar(label='Tegangan (V)')
plt.title('Solusi Persamaan Laplace 2D(Metode Jacobi)')
plt.show()

