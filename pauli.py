import numpy as np

# Define the Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]])
sigma_y = np.array([[0, -1j], [1j, 0]])
sigma_z = np.array([[1, 0], [0, -1]])

# Function to calculate eigenvalues and eigenvectors of a matrix
def eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Calculate eigenvalues and eigenvectors of the Pauli matrices
eigenvalues_x, eigenvectors_x = eigen(sigma_x)
eigenvalues_y, eigenvectors_y = eigen(sigma_y)
eigenvalues_z, eigenvectors_z = eigen(sigma_z)

# Print the results
print("Eigenvalues and eigenvectors of Pauli-X matrix:")
print("Eigenvalues:", eigenvalues_x)
print("Eigenvectors:", eigenvectors_x)
print()
print("Eigenvalues and eigenvectors of Pauli-Y matrix:")
print("Eigenvalues:", eigenvalues_y)
print("Eigenvectors:", eigenvectors_y)
print()
print("Eigenvalues and eigenvectors of Pauli-Z matrix:")
print("Eigenvalues:", eigenvalues_z)
print("Eigenvectors:", eigenvectors_z)
