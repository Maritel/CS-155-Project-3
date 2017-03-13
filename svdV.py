import numpy as np

V = np.load('V.npy')
A, sigma, B = np.linalg.svd(V)

proj = np.dot(A[0:2, :], V)

np.save('proj', proj)