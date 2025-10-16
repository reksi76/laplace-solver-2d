import numpy as np 

def laplace_jacobi(phi, max_iter=10000, tol=1e-5):
    new_phi = phi.copy()

    for it in range(max_iter):
        old_phi = new_phi.copy()
        new_phi[1:-1, 1:-1] = 0.25 * (old_phi[2:, 1:-1] + old_phi[:-2,1:-1] + old_phi[1:-1, 2:] + old_phi[1:-1,:-2])

        diff = np.max(np.abs(new_phi - old_phi))
        if diff < tol:
            break
    return it, new_phi

def laplace_gauss_seidle(phi, max_iter=10000, tol=1e-5, save_interval=50):
    history = []
    for it in range(max_iter):
        old_phi = phi.copy()
        phi[1:-1, 1:-1] = 0.25 * (phi[2:,1:-1] + phi[:-2, 1:-1] + phi[1:-1, 2:] + phi[1:-1, :-2])

        if it % save_interval == 0:
            history.append(phi.copy())

        diff = np.abs(np.max(phi - old_phi))
        if diff < tol:
            break
    return it, phi, history
        



