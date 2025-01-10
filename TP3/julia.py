import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la fractale
width, height = 800, 800 
x_min, x_max = -2, 2  
y_min, y_max = -2, 2  
max_iter = 256  

# Paramètre c pour l'ensemble de Julia (un nombre complexe)
c = complex(-0.8, 0.156)

# Création de l'image
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y  

# Initialisation de l'image de sortie
image = np.zeros(Z.shape, dtype=int)

# Fonction pour calculer l'itération de Julia
for i in range(max_iter):
    Z = Z**2 + c
    mask = np.abs(Z) > 2  
    image[mask] = i  

# Affichage de la fractale
plt.figure(figsize=(10, 10))
plt.imshow(image, cmap='inferno', extent=(x_min, x_max, y_min, y_max))
plt.colorbar()
plt.title("Fractale de Julia")
plt.show()
