import numpy as np

# Define the Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]])
sigma_y = np.array([[0, -1j], [1j, 0]])
sigma_z = np.array([[1, 0], [0, -1]])

# Function to calculate eigenvalues and eigenvectors of a matrix
def eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Function to Calculate the diagonal representation of Pauli matrices
def diagonal(eigenvalues,eigenvectors,matrix):
    diagonal_matrix = np.diag(eigenvalues)
    diagonalized_matrix = np.linalg.inv(eigenvectors) @ matrix @ eigenvectors
    return diagonal_matrix, diagonalized_matrix

# Calculate eigenvalues and eigenvectors of the Pauli matrices
eigenvalues_x, eigenvectors_x = eigen(sigma_x)
eigenvalues_y, eigenvectors_y = eigen(sigma_y)
eigenvalues_z, eigenvectors_z = eigen(sigma_z)

# Calculate the diagonal and diagonalized matrices of Pauli matrices
diagonal_x, diagonalized_x = diagonal(eigenvalues_x,eigenvectors_x,sigma_x)
diagonal_y, diagonalized_y = diagonal(eigenvalues_y,eigenvectors_y,sigma_y)
diagonal_z, diagonalized_z = diagonal(eigenvalues_z,eigenvectors_z,sigma_z)


# Print the results
print("Eigenvalues and eigenvectors of Pauli-X matrix:")
print("Eigenvalues:", eigenvalues_x)
print("Eigenvectors:", eigenvectors_x)
print("diagonal:", diagonal_x)
print("diagonalized:", diagonalized_x)
print()
print("Eigenvalues and eigenvectors of Pauli-Y matrix:")
print("Eigenvalues:", eigenvalues_y)
print("Eigenvectors:", eigenvectors_y)
print("diagonal:", diagonal_y)
print("diagonalized:", diagonalized_y)
print()
print("Eigenvalues and eigenvectors of Pauli-Z matrix:")
print("Eigenvalues:", eigenvalues_z)
print("Eigenvectors:", eigenvectors_z)
print("diagonal:", diagonal_z)
print("diagonalized:", diagonalized_z)
