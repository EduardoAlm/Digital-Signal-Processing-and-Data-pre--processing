import numpy as np
import matplotlib.pyplot as plt

# this code equal the faster version in the DFT matrix matlab file
n = 1024
w = np.exp(-1j*2*np.pi/n)

J, K = np.meshgrid(np.arange(n), np.arange(n))
DFT = np.power(w, J*K)
DFT = np.real(DFT)

plt.imshow(DFT)
plt.show()
