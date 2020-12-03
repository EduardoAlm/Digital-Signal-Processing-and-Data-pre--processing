import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
import imagesc as imagesc
from scipy.sparse import csr_matrix

def forw_function(n, s):
    id1 = np.linspace(1, n, n)
    w = np.zeros([n, n])
    for j in range(n):
        w[:, j] = np.exp(pow(id1 - (j + 1), 2) * (2 * pow(np.pi, 2)) / (pow(s, 2)))
    diagonals = np.linspace(0, pow(n, 2)-n, n)
    t_w = np.transpose(w)
    diag = sp.diags(t_w.diagonal(0), diagonals.astype(int), (n, pow(n, 2))).toarray()
    b = np.full((n, pow(n, 2)), diag)
    plt.spy(b)
    plt.show()
    return b
