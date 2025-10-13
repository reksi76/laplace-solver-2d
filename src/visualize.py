import matplotlib.pyplot as plt 

def plot_heatmap(phi):
    plt.imshow(phi, origin='lower', cmap='hot')
    plt.colorbar(label='Tempetature')
    plt.title('Laplace Equation Solution (2D)')
    plt.show()
