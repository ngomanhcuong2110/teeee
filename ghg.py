import numpy as np
from numpy import linalg as la

w, v = la.eig(np.array([[1,-1,0],[0,0,1],[0,0,0]]))

# Danh sách trị riêng
print("Eigenvalues: ")
print(w)
# Danh sách vector riêng
print("Eigenvectors: ")
print(v)