import matplotlib.pyplot as plt
import scipy as sp
from forw import forw_function
import numpy as np


def stft_function(x, s):
    n = len(x)
    g = forw_function(n, s)
    # a_fun = (lambda e1: (g * np.reshape(np.real(np.fft.ifft(np.reshape(e1, n, n))), pow(n, 2), 1)))
    at_fun = (lambda e1: np.reshape(np.fft.fft(np.reshape(np.transpose(g)*e1[:], (n, n))), (pow(n, 2), 1)))
    # tfx = np.zeros(pow(n, 2), 1) -> these values will be erased on the next line
    tfx = at_fun(x)
    tfx = np.reshape(tfx, (n, n))
    # recx = np.real(A(tfx)) -> never used
    return tfx
