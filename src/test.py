import numpy as np

N = 5
V0 = 100.0
max_iter = 10
tol = 1e-3

phi = np.zeros((N, N))
phi[-1, :] = V0  # boundary atas = 100

print("Iterasi ke-0:")
print(phi)
print()

for it in range(1, max_iter + 1):
    phi_new = phi.copy()
    for i in range(1, N-1):
        for j in range(1, N-1):
            phi_new[i, j] = 0.25 * (phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1])

    diff_array = phi_new - phi
    diff = np.max(np.abs(diff_array))
    print(f"Iterasi ke-{it}: diff max = {diff:.4f}")
    print("Perubahan tiap titik (phi_new - phi):")
    print(diff_array)
    print("Nilai phi setelah update:")
    print(phi_new)
    print()

    if diff < tol:
        print(f"Konvergen pada iterasi ke-{it}")
        break

    phi = phi_new
