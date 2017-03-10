import numpy as np

V = np.load('V.npy')
A, sigma, B = np.linalg.svd(V)

print(B.shape)

B_proj = B[0:2, :]
np.save('B_proj', B_proj)