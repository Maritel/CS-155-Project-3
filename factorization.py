import numpy as np
from prob2utils import train_model

# Here we obtain matrices U and V, such that U^T V approximates Y

m = 943  # number of users
n = 1682  # number of movies

# other dimension of U and V; U should be (k, m); V should be (k, n)
k = 20

data = np.load('data/data.npy')

# learning rate of 0.01 is good for many applications
# regularization coefficient is 0.01 arbitrarily
U, V, error = train_model(m, n, k, eta=0.01, reg=0.01, Y=data)

np.save('U', U)
np.save('V', V)
print(error)
